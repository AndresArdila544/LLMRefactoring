```python
class Dice:
    def __init__(self, dice):
        self.dice = dice

    def roll(self, direction):
        tmp = self.dice[:]
        if direction == "N":
            self.dice[0], self.dice[1], self.dice[4], self.dice[5] = tmp[1], tmp[5], tmp[0], tmp[4]
        elif direction == "E":
            self.dice[0], self.dice[2], self.dice[3], self.dice[5] = tmp[3], tmp[0], tmp[5], tmp[2]
        elif direction == "W":
            self.dice[0], self.dice[2], self.dice[3], self.dice[5] = tmp[2], tmp[5], tmp[0], tmp[3]
        else:
            self.dice[0], self.dice[1], self.dice[4], self.dice[5] = tmp[4], tmp[0], tmp[5], tmp[1]
    
    def check_dice(self, another):
        for dire in "NNNNWNNNWNNNENNNENNNWNNN":
            self.roll(dire)
            if self.dice == another.dice:
                return True
        return False
    
dice1 = Dice(list(map(str, input().split()))
dice2 = Dice(list(map(str, input().split())
if Dice.check_dice(dice1, dice2):
    print("Yes")
else:
    print("No")
```