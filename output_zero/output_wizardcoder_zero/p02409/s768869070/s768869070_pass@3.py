n = int(input())
for i in range(n):
    b, f, r, v = map(lambda x: int(x), input().split(" "))
    B, F, R = b - 1, f - 1, r - 1
    rooms[B][F][R] += v
for i in range(4):
    print("####################")
    for j in range(3):
        print(" ".join(map(str, rooms[i][j]))