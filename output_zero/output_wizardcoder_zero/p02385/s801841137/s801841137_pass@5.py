class Dice :
    def __init__(self, dice):
        self.dice = dice
        
    def roll(self, direction, index=None):
        if not index and direction in "NSEW":
            index = {"N": 0, "S": 1, "E": 2, "W": 3}.get(direction)
        elif not index: 
            return None
        self.dice[index], self.dice[(index+4)%6] = self.dice[(index+1)%6], self.dice[index] if direction == "N" else self.dice[index-2]
        
    def check_dice(self, another):
        for dire in "NNNNWNNNWNNNENNNENNNWNNN":
            if self.roll("N") == another.dice:
                return True
        return False
    
    def get_dice_nums(self):
        return self.dice
    
    def dice_top(self, index=0):
        print(self.dice[index])
        
dice1 = Dice(list(map(str, input().split()))
dice2 = Dice(list(map(str, input().split())
judge = dice1.check_dice(dice2)
print("Yes" if judge else "No")