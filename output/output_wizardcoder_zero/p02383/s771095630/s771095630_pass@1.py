class Dice:
    def __init__(self):
        self.d = [int(i) for i in input().split()]

    def e(self):
        self.d[0], self.d[2], self.d[3], self.d[5] = self.d[3], self.d[0], self.d[5], self.d[2]

    def w(self):
        self.d[0], self.d[2], self.d[3], self.d[5] = self.d[2], self.d[5], self.d[0], self.d[3]

    def n(self):
        self.d[0], self.d[1], self.d[4], self.d[5] = self.d[1], self.d[5], self.d[0], self.d[4]

    def s(self):
        self.d[0], self.d[1], self.d[4], self.d[5] = self.d[4], self.d[0], self.d[5], self.d[1]

def main():
    dice = Dice()
    for o in input():
        if   o == 'E': dice.e()
        elif o == 'W': dice.w()
        elif o == 'S': dice.s()
        else: dice.n()
    print(dice.d[0])

if __name__ == "__main__": main()