class Dice(object):
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.sides = (s1, s2, s3, s4, s5, s6)

    def rotate(self):
        self.sides = self.sides[::-1]

    def north(self):
        temp = self.sides[0]
        self.sides[0] = self.sides[4]
        self.sides[4] = temp
    
    def west(self):
        temp = self.sides[1]
        self.sides[1] = self.sides[5]
        self.sides[5] = temp
    
    def isSameDice(self, anotherDice):
        return self.sides == anotherDice.sides

s1, s2, s3, s4, s5, s6 = map(int, input().split())
dice1 = Dice(s1, s2, s3, s4, s5, s6)
s1, s2, s3, s4, s5, s6 = map(int, input().split())
dice2 = Dice(s1, s2, s3, s4, s5, s6)

flag = False
for j in range(6):
    if j % 2 == 0:
        dice2.north()
    else:
        dice2.west()

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