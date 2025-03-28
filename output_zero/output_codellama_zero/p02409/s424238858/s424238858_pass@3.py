Here's the refactored version of the code:

rooms = [[[0 for _ in range(10)] for __ in range(3)] for ___ in range(4)]
n = int(input())
for l in range(n):
    a,b,c,d = map(int, input().split())
    rooms[a-1][b-1][c-1] += d
for room in rooms:
    for row in room:
        print(" ".join(str(col) for col in row))
        if row != [0]*10 or room != [[0]*10]*3:
            print("####################")