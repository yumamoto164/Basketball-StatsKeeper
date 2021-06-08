class Player():
    def __init__(self, team, number, name):
        self.team = team
        self.number = number
        self.name = name
        
    def getTeam(self):
        return self.team
    
    def getNumber(self):
        return self.number
    
    def getName(self):
        return self.name
    
    
class Shot():
    def __init__(self, index, team, player_name, player_number, make, x, y, contested):
        self.index = index
        self.team = team # String
        self.player_name = player_name
        self.player_number = player_number
        self.make = make # Boolean 0: miss, 1: make
        self.x = x
        self.y = y
        self.contested = contested # Boolean 0: not contested, 1: contested
        
    def getIndex(self):
        return self.index
        
    def getTeam(self):
        return self.team
    
    def getPlayerName(self):
        return self.player_name
    
    def getPlayerNumber(self):
        return self.player_number
    
    def getMake(self):
        return self.make
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getContested(self):
        return self.contested
    