import math
x1, y1, x2, y2 = map(float, input().split())
d = math.hypot(x1-x2, y1-y2)
print(d)

n = int(input())
for i in range(1, n+1):
    if i % 3 == 0 or '3' in str(i):
        print('', i, end='')

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

while True:
    
    H,W = map(int,input().split())
    
    if H==0 and W==0:
        break
    
    for i in range(H):
        for j in range(W):
            if (i+j)%2 ==1:
                print(".",end='')
            else:
                print("#",end='')
        print()
    print()