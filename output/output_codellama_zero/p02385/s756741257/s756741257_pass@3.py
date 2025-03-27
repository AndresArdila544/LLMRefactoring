Here is a refactored version of the code:
```
dice1 = list(map(int, input().split()))
dice2 = list(map(int, input().split()))
eq = 0

def move(x):
    if x == 0 or x == 4:
        d[0], d[1], d[2], d[3], d[4], d[5] = d[1], d[5], d[2], d[3], d[0], d[4]
    elif x == 1 or x == 5:
        d[0], d[1], d[2], d[3], d[4], d[5] = d[2], d[1], d[5], d[0], d[4], d[3]
    elif x == 2 or x == 6:
        d[0], d[1], d[2], d[3], d[4], d[5] = d[3], d[1], d[0], d[5], d[4], d[2]
    elif x == 3:
        d[0], d[1], d[2], d[3], d[4], d[5] = d[4], d[0], d[2], d[3], d[5], d[1]

d = [dice1[0], dice1[1], dice1[2], dice1[3], dice1[4], dice1[5]]
for i in range(6):
    move(i)
    if d == dice2:
        eq = 1
        break
    else:
        for j in range(4):
            move(6)
        if d == dice2:
            eq = 1
            break
d = [dice1[0], dice1[1], dice1[2], dice1[3], dice1[4], dice1[5]]

if eq == 0:
    print("No")
else:
    print("Yes")
```