import sys
a = list(map(int, input().split()))
dir = input()
class Dise:
    def __init__(self, a):
        self.dise = a
    def roll(self, dir):
        for i in range(len(dir)):
            if dir[i] == "N":
                self.dise[0],self.dise[1],self.dise[4],self.dise[5] = self.dise[1],self.dise[5],self.dise[0],self.dise[4]
            elif dir[i] == "S":
                self.dise[0],self.dise[1],self.dise[4],self.dise[5] = self.dise[4],self.dise[0],self.dise[5],self.dise[1]
            elif dir[i] == "E":
                self.dise[0],self.dise[2],self.dise[3],self.dise[5] = self.dise[3],self.dise[0],self.dise[5],self.dise[2]
            elif dir[i] == "W":
                self.dise[0],self.dise[2],self.dise[3],self.dise[5] = self.dise[2],self.dise[5],self.dise[0],self.dise[3]
    def output(self):
        print(self.dise)

dise = Dise(a)
dise.roll(dir)
dise.output()