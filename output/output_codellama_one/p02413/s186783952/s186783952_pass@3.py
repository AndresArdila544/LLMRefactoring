import math
x1, y1, x2, y2 = map(float, input().split())
d = math.hypot(x1-x2, y1-y2)
print(d)

r, c = map(int, input().split())
a = []
for i in range(r):
    a.append(list(map(int, input().split())))
    a[i] += [sum(a[i])]
    print(*a[i])
a = list(zip(*a[::-1]))

for i in range(c):
    print(sum(a[i]), end=' ')
print(sum(a[c]))