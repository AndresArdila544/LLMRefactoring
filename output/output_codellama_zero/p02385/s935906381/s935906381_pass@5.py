class Dice(object):
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6

    def rotate(self, clockwise=True):
        if clockwise:
            self.s1, self.s2, self.s3, self.s4, self.s5, self.s6 = \
                self.s2, self.s3, self.s4, self.s5, self.s6, self.s1
        else:
            self.s1, self.s2, self.s3, self.s4, self.s5, self.s6 = \
                self.s6, self.s5, self.s4, self.s3, self.s2, self.s1

    def move(self, direction="north"):
        if direction == "north":
            self.rotate()
        elif direction == "west":
            self.rotate(clockwise=False)

    def isSameDice(self, anotherDice):
        return self.s1 == anotherDice.s1 and \
               self.s2 == anotherDice.s2 and \
               self.s3 == anotherDice.s3 and \
               self.s4 == anotherDice.s4 and \
               self.s5 == anotherDice.s5 and \
               self.s6 == anotherDice.s6

s1, s2, s3, s4, s5, s6 = map(int, input().split())
dice1 = Dice(s1, s2, s3, s4, s5, s6)
s1, s2, s3, s4, s5, s6 = map(int, input().split())
dice2 = Dice(s1, s2, s3, s4, s5, s6)

flag = False
for j in range(6):
    if j % 2 == 0:
        dice2.move("north")
    else:
        dice2.move("west")

    for k in range(4):
        dice2.rotate()
        if dice2.isSameDice(dice1):
            flag = True
            break
    if flag:
        break

if flag:
    print("Yes")
else:
    print("No")