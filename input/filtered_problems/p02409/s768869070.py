rooms = [[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
         [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
         [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
         [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
         ]
n = int(input())
for i in range(n):
    b, f, r, v = map(lambda x: int(x), input().split(" "))
    B, F, R = b - 1, f - 1, r - 1
    new = rooms[B][F][R] + v
    rooms[B][F][R] = new < 0 if 0 else new
for i in range(4):
    if 0 < i:
        print("####################")
    for j in range(3):
        print(" " + " ".join(map(lambda x: str(x), rooms[i][j])))

