import random

class Spinner:
    message = ""
    @staticmethod
    def spin():
        num = random.randint(1, 7)
        if num == 1:
            Spinner.message = "Take 1 cherry from the tree"
            return 1
        elif num == 2:
            Spinner.message = "Take 2 cherries from the tree"
            return 2
        elif num == 3:
            Spinner.message = "Take 3 cherries from the tree"
            return 3
        elif num == 4:
            Spinner.message = "Take 4 cherries from the tree"
            return 4
        elif num == 5:
            Spinner.message = ("Oh no, a dog has come and eaten some of your cherries. "
                               "Put 3 cherries back on your tree")
            return -3
        elif num == 6:
            Spinner.message = ("Oh no, a bird has come and eaten some of your cherries. "
                               "Put 2 cherries back on your tree")
            return -2
        else:  
            Spinner.message = ("Oh no, your basket spilled! Put all of your cherries back on your tree")
            return -10

    @staticmethod
    def getMessage():
        return Spinner.message


class Player:
    def __init__(self, name):
        self.name = name
        self.tree_cherries = 10
        self.bucket_cherries = 0

    #accessor methods
    def get_name(self): 
        return self.name

    def get_tree_cherries(self):
        return self.tree_cherries

    def get_bucket_cherries(self):
        return self.bucket_cherries

    def has_won(self):
        return self.bucket_cherries == 10

    def set_cherries(self, spin_value):
        if spin_value > 0:
            transfer = min(spin_value, self.tree_cherries)
            self.tree_cherries -= transfer
            self.bucket_cherries += transfer
        elif spin_value == -10:
            self.tree_cherries += self.bucket_cherries
            self.bucket_cherries = 0
        else:  
            amount = min(abs(spin_value), self.bucket_cherries)
            self.bucket_cherries -= amount
            self.tree_cherries += amount

    def __str__(self):
        return f"{self.name}: tree = {self.tree_cherries}, bucket = {self.bucket_cherries}"


def main():
    p1 = Player("Jiening")
    p2 = Player("Sofia")
    players = [p1, p2] #Use an array so it's easy to switch between turns

    print("Starting Hi Ho! Cherry-O!\n")
    turn = 0
    while True:
        current = players[turn % 2]
        outcome = Spinner.spin()
        print(f"{current.name} spins: {Spinner.getMessage()}") #The spinner text from the class
        current.set_cherries(outcome) #The method in the player class which does the actual stuff
        print("  ", current) #the "toString" method
        if current.has_won():
            print(f"\n{current.name} has won the game!")
            break
        turn += 1


if __name__ == "__main__":
    main()