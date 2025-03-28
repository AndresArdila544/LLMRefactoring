Here is the refactored version of the code:

class Dice():
    def __init__(self):
        self.number = [i for i in range(6)]
        self.work = [i for i in range(6)]
        self.order = 'NNNNWNNNWNNNENNNENNNWNNN'

    def setNumber(self, *args):
        for i, n in enumerate(args):
            self.number[i] = n

    def roll(self, loc):
        for i in range(6):
            self.work[i] = self.number[i]
        if loc == 'E':
            self.setNumber(self.work[3], self.work[1], self.work[0], self.work[5], self.work[4], self.work[2])
        elif loc == 'N':
            self.setNumber(self.work[1], self.work[5], self.work[2], self.work[3], self.work[0], self.work[4])
        elif loc == 'S':
            self.setNumber(self.work[4], self.work[0], self.work[2], self.work[3], self.work[5], self.work[1])
        elif loc == 'W':
            self.setNumber(self.work[2], self.work[1], self.work[5], self.work[0], self.work[4], self.work[3])

    def equals(self, another):
        for i in range(6):
            if self.number[i] != another.number[i]:
                return False
        return True

diceA = Dice()
diceB = Dice()

table = list(map(int, input().split()))
diceA.setNumber(*table)

table = list(map(int, input().split()))
diceB.setNumber(*table)

if diceA.equals(diceB):
    print("Yes")
else:
    print("No")