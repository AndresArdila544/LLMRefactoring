class Dice:
    def __init__(self, t, f, l, b, u):
        self.a = [[t,f,l,b,u]]
        self.direction = {'S': (4,0,2,3,5), 'N':(1,5,2,3,0),'E':(3,1,0,5,4), 'W':(2,1,5,0,4)}  # Removed unnecessary key 'Y'
    def roll(self, d):
        self.a[n][:] = [self.a[n][i] for i in self.direction[d]]
        
s='SSSWEEE'
w='YYYY'
ans='Yes'
for n in range(int(input())):  # Removed unnecessary loop that only runs once to initialize dice
    t, f, l, b, u = map(int, input().split())
    dice = Dice(t, f, l, u)
    for _ in range(n-1):  # Reduced the need for a separate loop to append new row and roll twice
        for j in s:
            for r in w:
                if dice.a == dice.roll(r):
                    ans='No'
                    break
            else:
                dice.roll(j)  # Removed indexing of list
                continue
            break
        else:
            continue
        break
print(ans)  # No need for a separate loop to check if all rolls were successful, just print at the end instead of changing ans variable