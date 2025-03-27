# ITP_11_C
class Dice :
    def __init__(self, dice) :
        self.dice = dice
    def roll(self, direction):
        tmp = self.dice[:]
        if direction == "N":
            self.dice[0] = tmp[1]
            self.dice[1] = tmp[5]
            self.dice[4] = tmp[0]
            self.dice[5] = tmp[4]
        elif direction == "E":
            self.dice[0] = tmp[3]
            self.dice[2] = tmp[0]
            self.dice[3] = tmp[5]
            self.dice[5] = tmp[2]
        elif direction == "W":
            self.dice[0] = tmp[2]
            self.dice[2] = tmp[5]
            self.dice[3] = tmp[0]
            self.dice[5] = tmp[3]
        else:
            self.dice[0] = tmp[4]
            self.dice[1] = tmp[0]
            self.dice[4] = tmp[5]
            self.dice[5] = tmp[1]

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
    def get_dice_nums(self):
        return(self.dice)
    
    def dice_top(self):
        print(self.dice[0])
    
dice1 = Dice(list(map(str, input().split())))
dice2 = Dice(list(map(str, input().split())))

judge = dice1.check_dice(dice2)
if judge == True:
    print("Yes")
else:
    print("No")
