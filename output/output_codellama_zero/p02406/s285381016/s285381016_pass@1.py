import math
n = int(input())
a = []
for i in range(1, n+1):
    if i % 3 == 0:
        a.append(i)
    elif i % 10 == 3:
        a.append(i)
print(*a)