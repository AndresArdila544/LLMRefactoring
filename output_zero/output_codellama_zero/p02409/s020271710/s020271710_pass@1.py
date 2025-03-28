n = int(input())
listA = [list(map(int, input().split(" "))) for i in range(n)]
b = [[[0]*10 for _ in range(3)] for _ in range(4)]
for i in listA:
    b[i[0]-1][i[1]-1][i[2]-1] += i[3]
for building in b:
    print(" " + " ".join(map(str, building)))
    if building != b[-1]:
        print("#" * 20)