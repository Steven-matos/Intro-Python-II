from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons!",
                     [Item('door', 'An old wooden door')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item('flashlight', 'An item to light your way')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item('telescope', 'view finder for long distance')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item('candles', 'Lights the passage forward')]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item('map', 'A dusty map that shows were the treasure was moved to.')]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main

# Make a new player object that is currently in the 'outside' room.
user_name = input("Name your player: ")

player = Player(user_name, room['outside'])

print(
    f"Welcome, {player.name} you are at {player.room}Item in room: '{player.room.items[0].name}'\n")
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    commands = input(
        "Choose you direction(n/s/e/w)\nIf in a room choose to (take) or (drop) an item by name.\nCheck your inventory with (i)\nYou may quit at any time with (q).\nYour choice:  ").lower().split(" ")
    if commands[0] in ["n", "s", "e", "w"]:
        # Move to that room
        player.travel(commands[0])
    elif commands[0] in ["take"]:
        if commands[1] != player.room.items[0].name:
            print("\nNot a item in existence!\n")
        else:
            item_name = commands[1]
            player.take(item_name)
    elif commands[0] in ["drop"]:
        item_name = commands[1]
        player.drop(item_name)
    elif commands[0] in ["i"]:
        player.inventory()
    elif commands[0] == "q":
        print("Thanks for playing!")
        exit()
    else:
        print("\nYou are getting me lost choose corretly.\n")
