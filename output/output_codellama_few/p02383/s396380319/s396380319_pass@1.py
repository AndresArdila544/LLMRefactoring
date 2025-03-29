import math
x1, y1, x2, y2 = map(float, input().split())
d = math.hypot(dx, dy)
print(d)

n = int(input())
for i in range(1, n+1):
    if i % 3 == 0 or '3' in str(i):
        print('', i, end='')
print()

n,m,l = map(int,input().split())
YEAH = [list(map(int,input().split())) for i in range(n)]
FUCK = [list(map(int,input().split())) for i in range(m)]

for i in range(n):
    GOMI_list = []
    for j in range(l):
        GOMI = 0
        for k in range(m):
            GOMI += FUCK[k][j]*YEAH[i][k]
        GOMI_list.append(GOMI)
    print(*GOMI_list,sep=' ')

dice = [int(_) for _ in input().split()]
move = [ _ for _ in input()]
dire = {"N": [2,6,3,4,1,5],"S":[5,1,3,4,6,2],
      "E":[4,2,1,6,5,3],"W":[3,2,6,1,5,4]}
em = []
for i in range(len(move)):
    em = dice[:]
    for j in range(len(dice)):
        em[j] = dice[dire[move[i]][j]-1]
    else:
        del dice[:]
        dice.extend(em)
print(dice[0])