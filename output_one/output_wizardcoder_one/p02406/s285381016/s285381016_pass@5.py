import math
n = int(input())
a = []
for i in range(1, n+1):
    if not (i % 3) and not (i % 10):
        a.append(i)
print(' ', end='')
print(*a)