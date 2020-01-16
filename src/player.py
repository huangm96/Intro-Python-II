# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def moving_direction(self, direction_cmd):
        new_room = self.room.get_room_in_direction(direction_cmd)
        if new_room is not None:
            self.room = new_room
            print(self.room)
        else:
            print("\nYou cannot go there!")

