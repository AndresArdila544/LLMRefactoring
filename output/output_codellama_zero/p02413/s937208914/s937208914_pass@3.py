Here is the refactored code:

a = []
gyou = []
retu = []
s = 0

c, r = map(int, input().split())

for i in range(r):
    gyou.append(0)

for i in range(c):
    a.append([])
    for j in range(r):
        a[i].append(int(input()))

for i in range(c):
        retu.append(sum(a[i]))

for i in range(r):
    for j in range(c):
        gyou[i] += a[j][i]

s = sum(gyou)

for i in range(c):
    print(" ".join([str(x) for x in a[i]]), retu[i])

    if i == c - 1:
        print(" ".join([str(x) for x in gyou]), s)