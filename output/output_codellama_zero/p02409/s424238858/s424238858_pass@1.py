# Here is the refactored version of the program:
rooms = [[[0] * 10 for _ in range(3)] for _ in range(4)]
n = int(input())
for l in range(n):
    a, b, c, d = map(int, input().split())
    rooms[a - 1][b - 1][c - 1] += d
for i in range(4):
    for j in range(3):
        print(*rooms[i][j], sep=" ", end="")
        if j != 2 or i != 3:
            print()
    if i != 3:
        print("####################")