import sys
input = sys.stdin.readline()
class Dice:
    def __init__(self, u, d, w, e, n):
        self.nums = {u: 'u', d: 'd', w: 'w', n: 'n'}
    
    def roll_w(self):
        self.nums['s'], self.nums['e'] = self.nums['s'], self.nums['n']
        self.nums['u'], self.nums['d'] = self.nums['u'], self.nums['e']
    
    def roll_e(self):
        self.nums['s'], self.nums['w'] = self.nums['s'], self.nums['d']
        self.nums['u'], self.nums['n'] = self.nums['u'], self.nums['e']
    
    def roll_s(self):
        self.nums['w'], self.nums['e'] = self.nums['w'], self.nums['n']
        self.nums['u'], self.nums['d'] = self.nums['u'], self.nums['s']
    
    def roll_n(self):
        self.nums['w'], self.nums['e'] = self.nums['w'], self.nums['s']
        self.nums['u'], self.nums['d'] = self.nums['u'], self.nums['n']
    
def main():
    a = list(map(int, input().split()))
    s = input()
    dice = Dice(*a)
    for c in s:
        if c == 'S':
            dice.roll_s()
        elif c == 'W':
            dice.roll_w()
        elif c == 'N':
            dice.roll_n()
    
    print(dice.nums['u'])

if __name__ == "__main__":
    main()