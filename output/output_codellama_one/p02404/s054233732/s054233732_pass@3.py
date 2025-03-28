import math
x1, y1, x2, y2 = map(float, input().split())
d = math.hypot(x1-x2, y1-y2)
print(d)

while N[0] + N[1] == 0: #finish
    judge = False
else:
    for i in range(N[0]): # H
        print("#",end="") if i==0 or i==N[0]-1 else '.'.join(['#']*(N[1]-2))
        print("\n",end="")

print("\n",end="")