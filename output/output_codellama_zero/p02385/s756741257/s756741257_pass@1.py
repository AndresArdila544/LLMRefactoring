def move(d, x):
    if x == 0: # N
        d[0], d[1], d[2], d[3], d[4], d[5] = (d[1], d[5], d[2], d[3], d[0], d[4])
    elif x == 1: # W
        d[0], d[1], d[2], d[3], d[4], d[5] = (d[2], d[1], d[5], d[0], d[4], d[3])
    elif x == 2: # E
        d[0], d[1], d[2], d[3], d[4], d[5] = (d[3], d[1], d[0], d[5], d[4], d[2])
    elif x == 3: # S
        d[0], d[1], d[2], d[3], d[4], d[5] = (d[4], d[0], d[2], d[3], d[5], d[1])
    elif x == 4: # そのまま
        d[0], d[1], d[2], d[3], d[4], d[5] = (d[0], d[1], d[2], d[3], d[4], d[5])
    elif x == 5: # ひっくり返し
        d[0], d[1], d[2], d[3], d[4], d[5] = (d[5], d[4], d[2], d[3], d[1], d[0])
    elif x == 6: # 頂点維持のまま回転
        d[0], d[1], d[2], d[3], d[4], d[5] = (d[0], d[2], d[4], d[1], d[3], d[5])
    return d

dice1 = list(map(int, input().split()))
dice2 = list(map(int, input().split()))
eq = 0
for i in range(6):
    for j in range(4):
        move(dice1, i)
        if dice1 == dice2:
            eq = 1
            break
    if eq == 1:
        break
else:
    print("No")
if eq == 0:
    print("Yes")