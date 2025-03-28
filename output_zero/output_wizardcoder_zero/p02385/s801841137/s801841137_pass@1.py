```python
class Dice :
    def __init__(self, dice):
        self.dice = dice

    def roll(self, direction):
        tmp = self.dice[:]
        if direction == "N":
            self.dice[0], self.dice[1] = tmp[5], tmp[0]
            self.dice[4], self.dice[5] = tmp[0], tmp[4]
        elif direction == "E":
            self.dice[0], self.dice[2] = tmp[0], tmp[3]
            self.dice[3], self.dice[5] = tmp[0], tmp[2]
        elif direction == "W":
            self.dice[0], self.dice[2] = tmp[2], tmp[5]
            self.dice[3], self.dice[5] = tmp[3], tmp[0]
        else:
            self.dice[0], self.dice[4] = tmp[4], tmp[5]
            self.dice[1], self.dice[5] = tmp[0], tmp[1]

    def check_dice(self, another):
        for dire in "NNNNWNNNWNNNENNNENNNWNNN":
            self.roll(dire)
            if self.dice == another.dice:
                return True
        return False
    
    def dice_top(self):
        print(self.dice[0])
    
def main():
    dice1 = Dice([int(x) for x in input().split()])
    dice2 = Dice([int(x) for x in input().split()])
    judge = dice1.check_dice(dice2)
    if judge:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
```