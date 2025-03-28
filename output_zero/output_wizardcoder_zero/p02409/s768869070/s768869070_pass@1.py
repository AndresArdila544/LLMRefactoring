rooms = [[[0] * 7 for _ in range(3)] for _ in range(4)]
for _ in range(int(input())):
    b, f, r, v = map(lambda x: int(x) - 1, input().split())
    rooms[b][f], rooms[r] = [(rooms[b][f] + v) % 256 if rooms[b][f] + v >= 0 else 0 for i in range(2)]
for i in range(4):
    print(" ".join(str(x) for row in rooms[i] for x in row))
    if i != 3:
        print("####################")