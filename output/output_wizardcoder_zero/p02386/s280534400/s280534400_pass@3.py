class Dice:
    def __init__(self):
        self.num = [1] * 6
    
    def roll(self, d):
        if   d == "N":
            b = self.num[0]
            self.num[0], self.num[1], self.num[5] = self.num[1], self.num[5], self.num[4]
            self.num[4] = b
        elif d == "S":
            b = self.num[0]
            self.num[0], self.num[4], self.num[5] = self.num[4], self.num[5], self.num[1]
            self.num[1] = b
        elif d == "W":
            b = self.num[3]
            self.num[3], self.num[0], self.num[2] = self.num[0], self.num[2], self.num[5]
            self.num[5] = b
        elif d == "E":
            b = self.num[3]
            self.num[3], self.num[2], self.num[5] = self.num[2], self.num[5], self.num[0]
            self.num[0] = b
    
    def print_num(self, m):
        return self.num[m - 1]

N = int(input())
for n in range(N):
    lst = [int(i) for i in input().split()]
    dices = []
    for _ in range(N):
        dices.append(Dice())
    for dice1, dice2 in itertools.combinations(dices, 2):
        if all(dice1.roll(d) == dice2.roll(d) for d in buff):
            print("No")
            exit()
else:
    print("Yes")