class Dice:
    def __init__(self, lst):
        self.val = lst
    
    def rotate(self, dir):
        if dir == "N":
            tmp = self.val[0]
            self.val[0], self.val[1] = self.val[1], tmp
        elif dir == "E":
            tmp = self.val[3]
            self.val[3], self.val[5] = self.val[5], tmp
        elif dir == "S":
            tmp = self.val[4]
            self.val[4], self.val[5] = self.val[5], tmp
        elif dir == "W":
            tmp = self.val[2]
            self.val[2], self.val[5] = self.val[5], tmp
    
    def roll(self):
        for i in range(random.randint(0, 4)):
            self.rotate(int_to_dir(random.randint(0, 4)))


x = list(map(int, input().split()))
q = int(input())

dice = Dice(x)

for i in range(q):
    a, b = map(int, input().split())
    dice.roll()
    if dice.val[0] == a and dice.val[1] == b:
        print(dice.val[2])