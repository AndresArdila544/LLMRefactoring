```python
class Dice:
    def __init__(self, t, f, l, r, b, u):
        self.t = t
        self.f = f
        self.l = l
        self.r = r
        self.b = b
        self.u = u
        self.a = [t, f, l, r, b, u]
        self.direction = {'S': (4, 0, 2, 3, 5, 1), 'N': (1, 5, 2, 3, 0, 4), 'E': (3, 1, 0, 5, 4, 2), 'W': (2, 1, 5, 0, 4, 3), 'Y': (0, 3, 1, 4, 2, 5)}
    
    def roll(self, d):
        self.a = [self.a[i] for i in self.direction[d]]
        self.t = self.a[0]
        self.f = self.a[1]
        self.r = self.a[2]
        self.l = self.a[3]
        self.b = self.a[4]
        
s, w = input().split(), 'YYYY'
dice1, dice2 = Dice(*map(int, input().split())), Dice(*map(int, input().split())
for j in s:
    for r in w:
        if dice1.a == dice2.a:
            print('Yes')
            break
        else:
            dice2.roll(r)
    else:
        dice2.roll(j)
```