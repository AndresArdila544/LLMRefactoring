def is_dice_equal(d1, d2):
    if all(d1[i] == d2[(i+3)%6] for i in range(5)):
        return True
    else:
        for i in range(4):
            move(d1, 0)
            if d1 == d2:
                return True
    for j in range(4):
        move(d1, 6)
        if d1 == d2:
            return True
    return False

def move(dice, direction):
    # N
    if direction == 0:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0]
    # W
    elif direction == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4]
    # E
    elif direction == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[4], dice[5]
    # S
    elif direction == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5]
    # そのまま
    elif direction == 4:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[0], dice[1], dice[2], dice[3], dice[4]
    # ひっくり返し
    elif direction == 5:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[5], dice[4], dice[2], dice[3], dice[1]
    #頂点維持のまま回転
    elif direction == 6:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[0], dice[2], dice[4], dice[1], dice[3]

dice1 = list(map(int, input().split()))
dice2 = list(map(int, input().split())
if is_dice_equal(dice1, dice2):
    print("Yes")
else:
    print("No")