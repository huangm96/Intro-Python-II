# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        # n_to, s_to, e_to, w_to
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []
    
    def __str__(self):
        display = ""
        display += f"\nCurrent Room: {self.name}\n"
        display += f"\nDescription: {self.description}\n"
        return display
    
    def get_room_in_direction(self, direction_cmd):
        if hasattr(self, f"{direction_cmd}_to"):
            return getattr(self, f"{direction_cmd}_to")
        return None

        
