# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.backpack = []
    def travel(self, direction_cmd):
        new_room = self.room.get_room_in_direction(direction_cmd)
        if new_room is not None:
            self.room = new_room
            print(f"\n************************* WALKING ***************************")
            
        else:
            print("\n******************** You cannot go there! ************************\n")

    def pick_up_item(self, item):
        # if item is in the room, put it in backpack, and remove from the room
        if item in self.room.items:
            print(f"\n************** Picked_up {item}! ******************\n")
            self.backpack.append(item)
            self.room.items.remove(item)
            print(f"Your backpack: {self.backpack}")
        else:
            print("This item is not in the room!")
        

    def drop_item(self, item):
        # if item is in the backpack, remove from backpack and put it in the room
        if item in self.backpack:
            print(f"\n************** Dropped {item}! ******************\n")
            self.backpack.remove(item)
            self.room.items.append(item)
            print(f"Your backpack: {self.backpack}")
        else:
            print("This item is not in your backpack!")
        
