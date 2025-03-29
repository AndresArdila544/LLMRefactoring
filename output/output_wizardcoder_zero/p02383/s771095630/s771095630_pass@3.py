class Dice:
    def __init__(self, default = [1,2,3,4,5,6]):
        self.d = list(default)
        
    def e(self):
        self.d[0], self.d[2], self.d[3], self.d[5] = self.d[3], self.d[0], self.d[5], self.d[2]
        
    def w(self):
        self.d[0], self.d[2], self.d[3], self.d[5] = self.d[2], self.d[5], self.d[0], self.d[3]
        
    def n(self):
        self.d[0], self.d[1], self.d[4], self.d[5] = self.d[1], self.d[5], self.d[0], self.d[4]
        
    def s(self):
        self.d[0], self.d[1], self.d[4], self.d[5] = self.d[4], self.d[0], self.d[5], self.d[1]
        
    def top(self):
        return max(self.d)

def main():
    dice = Dice([int(i) for i in input().split()])
    ops = {'E': 'e', 'W': 'w', 'S': 's'}
    while True:
        try:
            op = input()
            if op == 'N':
                dice.n()
            else:
                getattr(dice, ops[op])()
        except (EOFError, KeyError):
            break
    print(dice.top())