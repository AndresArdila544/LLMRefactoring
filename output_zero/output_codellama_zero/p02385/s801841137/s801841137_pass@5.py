```
class Dice:
    def __init__(self, dice):
        self.dice = list(map(str, input().split()))
        
    def check_dice(self, another):
        for dire in "NNNNWNNNWNNNENNNENNNWNNN":
            self.roll(dire)
            if self.dice == another.dice:
                return True
        return False
    
    def get_dice_nums(self):
        return self.dice
    
    def dice_top(self):
        print(self.dice[0])
        
dice1 = Dice(input().split())
dice2 = Dice(input().split())

if dice1.check_dice(dice2):
    print("Yes")
else:
    print("No")
```