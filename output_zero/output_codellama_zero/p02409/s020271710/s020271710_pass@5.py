n = int(input())
listA = [list(map(int, input().split(" "))) for i in range(n)]

b = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
for i in listA:
    b[i[0]-1][i[1]-1][i[2]-1] += i[3]

for idx, building in enumerate(b):
    for floor in building:
        print(" " + " ".join(map(str, floor)))
    if idx < 3:
        print("#" * 20)