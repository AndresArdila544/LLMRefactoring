import math

class Dice:
    def __init__(self, t, f, r, l, b, u):
        self.a = [[t,f,r,l,b,u]]
        self.direction = {'S': (4,0,2,3,5,1), 'N': (1,5,2,3,0,4), 'E': (3,1,0,5,4,2), 'W': (2,1,5,0,4,3), 'Y': (0,3,1,4,2,5)}
    def roll(self, d, n):
        self.a[n] = [self.a[n][i] for i in self.direction[d]]
        
x= int(input())
dice_list = []
for _ in range(x):
    t, f, r, l, b, u = map(int, input().split())
    dice = Dice(t, f, r, l, b, u)
    dice_list.append(dice)
    
s='SSSWEEE'
w='YYYY'
for i in range(len(dice_list)-1):
    for j in s:
        for k in w:
            if dice_list[i].a == dice_list[i+1].a:
                ans='No'
                break
            dice_list[i+1].roll(k,i+1)
            else:
                dice_list[i+1].roll(j,i+1)
                continue
            break
        else:
            continue
        break
    else:
        continue
    break
else:
    print("Yes")