# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.room = starting_room
        self.items = []

    def travel(self, direction):
        next_room = getattr(self.room, f"{direction}_to")
        if next_room is not None:
            self.room = next_room
            print(f"{self.room}")
            print("Items: '{}'\n".format(
                ", ".join([item.name for item in self.room.items])))
        else:
            print("\nYou cannot move in that direction\n")

    def take(self, item_name):
        item = self.room.drop(item_name)
        self.items.append(item)
        item.on_take()
        return item

    def drop(self, item_name):
        item = self.find(item_name)
        self.items.remove(item)
        self.room.take(item)
        item.on_drop()
        return item

    def find(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item

    def inventory(self):
        print("\nInventory:\n")
        for idx, item in enumerate(self.items):
            print(f"  " + str(idx+1) + ") " + item.name)
