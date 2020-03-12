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

# Items in Rooms
room['foyer'].items = ['a sword']
room['treasure'].items = ['a silver key']



# Main
#
# Ask player's name
player_name = input("Welcome to the game! What's your name?\n~~>   ")
# Make a new player object that is currently in the 'outside' room.
player = Player(player_name, room=room['outside'])
# Greet player
print(f"\nHello, player: {player_name}.\n\n********************* Game starts! ****************************** ")


# commands rule
direction_rule = ["n", "s", "e", "w"]
action_rule = [1, 2, 3, 4]

# action_helper_function
def action_helper_function(action_cmd):
    # if player enters 1, pick up item
    if action_cmd == 1:
        # print no item if the room is empty
        if len(player.room.items) == 0:
            print("\n*********************** There is no item in this room! ************************")
        # pick up item
        else:
            picked_up_item = input("Please Enter the item's name that you want to pick up: ")
            player.pick_up_item(picked_up_item)

    # if player enters 2, drop off item
    elif action_cmd == 2:
        # print no item if player's backpack is empty
        if len(player.backpack) == 0:
            print("\n*********************** You do not have any item! **********************")
        # drop off item
        else:
            print(f"Your backpack: {player.backpack}")
            dropped_item = input("Please Enter the item's name that you want to drop down: ")
            player.drop_item(dropped_item)
    
    # if player enters 3, go to a new room
    elif action_cmd == 3:
        moving_cmd = ""
        while True:
            # Let player chooses direction:[n(north), s(south), w(west), e(east),q(quit)]
            moving_cmd = input("Please enter the direction: n(north), s(south), w(west), e(east),q(quit): \n~~>   ").lower()
            # if player enters q, go to upper level, let player chooses actions
            if moving_cmd == "q":
                break
            # if player enter wrong cmd, give warning
            elif not moving_cmd in direction_rule:
                print("\nWrong command! please re-enter:")
            # else 
            else:
                player.travel(moving_cmd)
                break
# Write a loop that:

action_cmd = ""


while True:
    # * Prints the current room info
    print(player.room)
# Let player chooses action:[1.pick_up item 2.drop item 3.leaving the room 4.quit the game]
    print('''Please enter the action:\n
   1.pick_up item \n   2.drop item \n   3.leaving the room \n   4.quit the game \n''' )
    
    # Waits for player input and decides what to do.
    action_cmd = int(input("~~>   "))
#     # If the player enters "4", quit the game.
    if action_cmd == 4:
        print(f"\nBye! player: {player_name}. Thank you for playing!\n")
        break
#     # If the player does not enter correct cmd, give warning.
    elif not action_cmd in action_rule:
        print("\nWrong command! please re-enter:")
    # else go to the action helper function.
    else:
        action_helper_function(action_cmd)
    

    
