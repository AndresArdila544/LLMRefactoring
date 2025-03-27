#Refactor the dice class to improve its readability and reduce it's complexity. This includes adding docstrings, comments, better variable names, etc.
#The main function should remain the same

class Dice:
    def __init__(self,dice):
        """Initialize the dice with a list of numbers (6 numbers)"""
        self.dice = dice
    
    def roll_n(self):
        """Rotate the dice clockwise 90 degrees"""
        d = self.dice
        self.dice = [d[1],d[5],d[2],d[3],d[0],d[4]]

    def roll_e(self):
        """Rotate the dice clockwise 90 degrees to the east"""
        d = self.dice
        self.dice = [d[3],d[1],d[0],d[5],d[4],d[2]]

    def roll_s(self):
        """Rotate the dice clockwise 90 degrees to the south"""
        d = self.dice
        self.dice = [d[4],d[0],d[2],d[3],d[5],d[1]]
    
    def roll_w(self):
        """Rotate the dice clockwise 90 degrees to the west"""
        d = self.dice
        self.dice = [d[2],d[1],d[5],d[0],d[4],d[3]]

    def top(self):
        return self.dice[0]