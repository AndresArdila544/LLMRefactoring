Here is a revised version of the code that has fewer lines and improved readability:
```
class Dice:
    def __init__(self, dice):
        self.dice = dice

    def roll(self, direction):
        tmp = self.dice[:]
        if direction == "N":
            self.dice[0], self.dice[1] = self.dice[1], self.dice[5]
            self.dice[4], self.dice[5] = self.dice[0], self.dice[4]
        elif direction == "E":
            self.dice[0], self.dice[2] = self.dice[3], self.dice[0]
            self.dice[3], self.dice[5] = self.dice[2], self.dice[3]
        elif direction == "W":
            self.dice[0], self.dice[2] = self.dice[2], self.dice[0]
            self.dice[3], self.dice[5] = self.dice[5], self.dice[3]
        else:
            self.dice[0], self.dice[1] = self.dice[4], self.dice[0]
            self.dice[4], self.dice[5] = self.dice[1], self.dice[5]

    def check_dice(self, another):
        for dire in "NNNNWNNNWNNNENNNENNNWNNN":
            self.roll(dire)
            check = True
            for i in range(6):
                if self.dice != another.dice:
                    check = False
                    break
            if check == True:
                break
        return check

dice1 = Dice(list(map(str, input().split())))
dice2 = Dice(list(map(str, input().split())))

judge = dice1.check_dice(dice2)
if judge == True:
    print("Yes")
else:
    print("No")
```