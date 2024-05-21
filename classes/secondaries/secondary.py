class Secondary:
    def __init__(self, name, description, is_available_turn_one):
        self.name = name
        self.description = description
        self.is_available_turn_one = is_available_turn_one
    
    def getName(self):
        return self.name
    
    def getDescription(self):
        return self.description
    
    def getIsAvailableTurnOne(self):
        return self.is_available_turn_one