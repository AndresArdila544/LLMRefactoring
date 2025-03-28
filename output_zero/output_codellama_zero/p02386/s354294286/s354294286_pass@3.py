class Dice:
    def __init__(self, t, f, r, l, b, u):
        self.a = [[t,f,r,l,b,u]]
        self.direction = {'S': (4,0,2,3,5,1), 'N':(1,5,2,3,0,4),'E':(3,1,0,5,4,2),'W':(2,1,5,0,4,3),'Y':(0,3,1,4,2,5)}
    def roll(self, d, n):
        self.a[n] = [self.a[n][i] for i in self.direction[d]]

n = int(input())
dice = Dice()
for _ in range(n):
    t, f, r, l, b, u = map(int, input().split())
    dice.a.append([t,f,r,l,b,u])
    for u in range(1, n+1):
        for t in range(u+1, n+1):
            for j in "SSSWEEE":
                for r in "YYYY":
                    if dice.a[t] == dice.a[u]:
                        ans = "No"
                        break
                    dice.roll(r, t)
                else:
                    dice.roll(j, t)
                    continue
            break
            break
        else:
            continue
        break
    else:
        continue
print("Yes")