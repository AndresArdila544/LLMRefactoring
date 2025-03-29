a = [int(i) for i in input().split()]
dise = a[1:]
for turn in input():
    if turn == "N":
        dise[0], dise[1], dise[4], dise[5] = dise[1], dise[5], dise[0], dise[4]
    elif turn == "S":
        dise[0], dise[1], dise[4], dise[5] = dise[4], dise[0], dise[5], dise[1]
    elif turn == "E":
        dise[0], dise[2], dise[3], dise[5] = dise[3], dise[0], dise[5], dise[2]
    elif turn == "W":
        dise[0], dise[2], dise[3], dise[5] = dise[2], dise[5], dise[0], dise[3]
print(dise[0])