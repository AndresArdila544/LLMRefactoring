n = int(input())
listA = [list(map(int, input().split(" "))) for i in range(n)]

b = []
f = []
r = []
v = []
for building in range(4):
    for floor in range(3):
        for room in range(10):
            r.append(0)
        f.append(r)
        r = []
    b.append(f)
    f = []

for i in listA:
    b[i[0]-1][i[1]-1][i[2]-1] += i[3]

for idx, building in enumerate(b):
    for floor in building:
        print(" " + " ".join(map(str, floor)))
    if idx < 3:
        print("#" * 20)

