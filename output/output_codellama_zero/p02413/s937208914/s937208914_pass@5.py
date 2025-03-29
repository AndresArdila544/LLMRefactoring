a = []
gyou = []
retu = []
s = 0

c, r = map(int, input().split())

for i in range(r):
    gyou.append(sum([x[i] for x in a]))

for i in range(c):
    retu.append(sum([y[i] for y in a]))

s = sum(gyou)

for i in range(c):
    print(" ".join(map(str, a[i])), retu[i], sep="")

if c == r - 1:
    print("".join(map(str, gyou)), s)