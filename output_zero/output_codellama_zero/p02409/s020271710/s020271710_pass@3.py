Here is the refactored version of the code:

n = int(input())
listA = [list(map(int, input().split(" "))) for i in range(n)]

b = [[[0] * 10 for _ in range(3)] for _ in range(4)]
for i in listA:
    b[i[0]-1][i[1]-1][i[2]-1] += i[3]

for building in b:
    for floor in building:
        print(" " + " ".join(map(str, floor)))
    if not building[-1]:
        print("#" * 20)