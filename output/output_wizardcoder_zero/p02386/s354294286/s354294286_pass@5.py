class Dice:
    def __init__(self, t, f, l, r, u):
        self.a = [[t, f, l, u] for _ in range(6)]
        
    def roll(self, d, n):
        if d == 'S':
            self.a[n][0], self.a[1], self.a[2], self.a[3] = self.a[4], self.a[0], self.a[2], self.a[5]
        elif d == 'N':
            self.a[n][0], self.a[1], self.a[2], self.a[3] = self.a[1], self.a[4], self.a[2], self.a[0]
        elif d == 'E':
            self.a[n][0], self.a[1], self.a[2], self.a[3] = self.a[5], self.a[1], self.a[0], self.a[3]
        elif d == 'W':
            self.a[n][0], self.a[1], self.a[2], self.a[3] = self.a[2], self.a[1], self.a[0], self.a[4]
        elif d == 'Y':
            self.a[n][0], self.a[1], self.a[2], self.a[3] = self.a[0], self.a[5], self.a[1], self.a[2]
        
    def roll_and_check(self, d):
        for i in range(6-1):
            if dice.a[i+1] == dice.a[i]:
                return False
            else:
                dice.roll(d, i)
        return True

n = int(input())
t, f, l, u = map(int, input().split())
dice = Dice(t, f, l, u)
s='SSSWEEE'
w='YYYY'
ans='Yes'
for i in range(1, n):
    a = list(map(int, input().split()))
    dice.a[i] = a
    
    if not dice.roll_and_check('Y'):
        ans = 'No'
        break
        
print(ans)