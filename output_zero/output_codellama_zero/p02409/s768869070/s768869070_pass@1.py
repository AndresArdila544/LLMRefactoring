Here is the refactored version of the code:

n = int(input())
for i in range(n):
    b, f, r, v = map(int, input().split(" "))
    rooms[b - 1][f - 1][r - 1] += v

    for row in rooms:
        print(" ".join(map(str, row)))