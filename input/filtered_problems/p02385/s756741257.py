dice1 = list(map(int,input().split()))
dice2 = list(map(int,input().split()))
eq = 0

def move(x):
    # N
    if x == 0:
        d[0],d[1],d[2],d[3],d[4],d[5] = d[1],d[5],d[2],d[3],d[0],d[4]
    # W
    elif x == 1:
        d[0],d[1],d[2],d[3],d[4],d[5] = d[2],d[1],d[5],d[0],d[4],d[3]

    # E
    elif x == 2:
        d[0],d[1],d[2],d[3],d[4],d[5] = d[3],d[1],d[0],d[5],d[4],d[2]
    # S
    elif x == 3:
        d[0],d[1],d[2],d[3],d[4],d[5] = d[4],d[0],d[2],d[3],d[5],d[1]

# そのまま
    elif x == 4:
        d[0],d[1],d[2],d[3],d[4],d[5] = d[0],d[1],d[2],d[3],d[4],d[5]
#ひっくり返し
    elif x == 5:
        d[0],d[1],d[2],d[3],d[4],d[5] = d[5],d[4],d[2],d[3],d[1],d[0]

#頂点維持のまま回転
    elif x == 6:
        d[0],d[1],d[2],d[3],d[4],d[5] = d[0],d[2],d[4],d[1],d[3],d[5]

d = [dice1[0],dice1[1],dice1[2],dice1[3],dice1[4],dice1[5]]
for i in range(6):
    move(i)
    if d == dice2:
        eq = 1
        break
    else:
        for j in range(4):
            move(6)

            if d == dice2:
                eq = 1
                break
    d = [dice1[0],dice1[1],dice1[2],dice1[3],dice1[4],dice1[5]]


if eq == 0:
    print("No")
else:
    print("Yes")
