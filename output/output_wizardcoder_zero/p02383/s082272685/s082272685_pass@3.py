import sys
class Dice:
    def __init__(self, u, d, w, e, n):
        self.nums = {'u': u, 'd': d, 'w': w, 'e': e, 'n': n}
        
    def roll_dice(self, side):
        if side == 'S':
            self.nums['s'], self.nums['n'] = self.nums['u'], self.nums['e']
            self.nums['u'], self.nums['e'] = self.nums['w'], self.nums['d']
        elif side == 'W':
            self.nums['s'], self.nums['n'] = self.nums['s'], self.nums['d']
            self.nums['u'], self.nums['e'] = self.nums['w'], self.nums['n']
        elif side == 'N':
            self.nums['w'], self.nums['e'] = self.nums['w'], self.nums['u']
            self.nums['u'], self.nums['d'] = self.nums['n'], self.nums['s']
        elif side == 'E':
            self.nums['w'], self.nums['s'] = self.nums['e'], self.nums['u']
            self.nums['u'], self.nums['d'] = self.nums['n'], self.nums['s']
        
    def print_results(self):
        return self.nums['u']
    
def main():
    u, d, w, e, n = map(int, input().split())
    s = input()
    dice = Dice(u, d, w, e, n)
    for side in s:
        dice.roll_dice(side)
    print(dice.print_results())

if __name__ == "__main__":
    main()