class Dice:
    def __init__(self, t, f, r, l, b, u):
        self.a = [[t, f, r, l, b, u]]
        self.direction = {'S': (4, 0, 2, 3, 5, 1), 'N': (1, 5, 2, 3, 0, 4), 'E': (3, 1, 0, 5, 4, 2), 'W': (2, 1, 5, 0, 4, 3), 'Y': (0, 3, 1, 4, 2, 5)}
    
    def roll(self, d, n):
        self.a[n] = [self.a[n][i] for i in self.direction[d]]
    
s = 'SSSWEEE'
w = 'YYYY'
ans = 'Yes'
for u in range(n - 1):
    for t in range(u + 1, n):
        for j in s:
            for r in w:
                if dice.a[t] == dice.a[u]:
                    ans = 'No'
                    break
                dice.roll(r, t)
            else:
                dice.roll(j, t)
                continue
            break
        else:
            continue
        break
    else:
        continue
    break
print(ans)