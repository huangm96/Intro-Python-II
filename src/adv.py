from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
#
# Ask player's name
player_name = input("Welcome to the game! What's your name?\n")
# Make a new player object that is currently in the 'outside' room.
player = Player(player_name, room=room['outside'])
# Greet player
print(f"Hello, player: {player_name}. Game start!\n")

# road_end_warning helper method
def road_end_warning():
    print("\nYou cannot go there!")

# walking helper method
def walking_print():
    print("\nWALK.............")
# commands rule
direction_rule = ["w", "a", "s", "d", "q"]



# Write a loop that:
moving = ""
while True:

# * Prints the current room name
    print("Current Room: ",player.room.name)
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
    moving = input("Please enter the direction: w(north), s(south), a(west), d(east), q(quit): \n")
# If the user enters a cardinal direction, attempt to move to the room there.
    if moving == "w":
        try:
            player.room = player.room.n_to
            walking_print()
        except:
            road_end_warning()
            
    elif moving == "a":
        try:
            player.room = player.room.w_to
            walking_print()
        except:
            road_end_warning()

    elif moving == "s":
        try:
            player.room = player.room.s_to
            walking_print()
        except:
            road_end_warning()

    elif moving == "d":
        try:
            player.room = player.room.e_to
            walking_print()
        except:
            road_end_warning()
# Print an error message if the movement isn't allowed.
    if not moving in direction_rule:
        print("\nWrong command! please re-enter:")
        
# If the user enters "q", quit the game.
    if moving == "q":
        print(f"\nBye! player: {player_name}\n")
        break
