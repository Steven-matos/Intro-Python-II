# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room, direction=None):
        self.name = name
        self.room = room
        self.direction = direction
        
    def movement(self, direction):
        move = getattr(self.room, f"{direction}_to")
        if move != None:
            self.room = move
            print(self.room)
        else:
            print("You ran into a wall try another direction")