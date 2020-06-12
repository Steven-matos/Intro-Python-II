class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f"\n\nYou have picked up a {self.name}\n\n")

    def on_drop(self):
        print(f"\n\nYou have dropped {self.name}\n\n")
