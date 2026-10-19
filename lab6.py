import random

class Board:
    @staticmethod
    def spin():
        return random.randint(1, 6)
    
    @staticmethod
    def getNewLocation(currentLocation):
        newLocation = Board.spin() + currentLocation
        if newLocation == 1:
            print("Ladder to 38")
            return 38
        elif newLocation == 4:
            print("Ladder to 14")
            return 14
        elif newLocation == 9:
            print("Ladder to 31")
            return 31
        elif newLocation == 16:
            print("Chute to 6")
            return 6
        elif newLocation == 21:
            print("Ladder to 42")
            return 42
        elif newLocation == 28:
            print("Ladder to 84")
            return 84
        elif newLocation == 36:
            print("Ladder to 44")
            return 44
        elif newLocation == 47:
            print("Chute to 26")
            return 26
        elif newLocation == 49:
            print("Chute to 11")
            return 11
        elif newLocation == 51:
            print("Ladder to 67")
            return 67
        elif newLocation == 56:
            print("Chute to 53")
            return 53
        elif newLocation == 62:
            print("Chute to 19")
            return 19
        elif newLocation == 64:
            print("Chute to 60")
            return 60
        elif newLocation == 71:
            print("Ladder to 91")
            return 91
        elif newLocation == 80:
            print("Ladder to 100")
            return 100
        elif newLocation == 87:
            print("Chute to 24")
            return 24
        elif newLocation == 93:
            print("Chute to 73")
            return 73
        elif newLocation == 95:
            print("Chute to 75")
            return 75
        elif newLocation == 98:
            print("Chute to 78")
            return 78
        
        if newLocation > 100:
            return currentLocation
        return newLocation
    
class Player:
    name = ""
    space = 0
    def setName(self, name):
        self.name = name
        self.space = 0

    def getName(self):
        return self.name
    
    def getSpace(self):
        return self.space
    
    def hasWon():
        return Player.getSpace == 100
    
    def __str__(self):
        return f"{self.name} is on space {self.space}"
    
def main():
    