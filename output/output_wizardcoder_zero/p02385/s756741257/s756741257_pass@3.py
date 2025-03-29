dice1 = list(map(int, input().split()))
dice2 = list(map(int, input().split())
eq = 0

def move(x):
    if x == 0:
        d[0], d[1], d[2], d[3], d[4], d[5] = d[1], d[5], d[2], d[3], d[0]
    elif x == 1:
        d[0], d[1], d[2], d[3], d[4], d[5] = d[2], d[1], d[5], d[0], d[4]
    elif x == 2:
        d[0], d[1], d[2], d[3], d[4], d[5] = d[3], d[1], d[0], d[5], d[4]
    elif x == 3:
        d[0], d[1], d[2], d[3], d[4], d[5] = d[4], d[0], d[2], d[3], d[5]
# そのまま
    elif x == 4:
        d[0], d[1], d[2], d[3], d[4], d[5] = d[0], d[1], d[2], d[3], d[4]
# ひっくり返し
    elif x == 5:
        d[0], d[1], d[2], d[3], d[4], d[5] = d[5], d[4], d[2], d[3], d[1]

d = [dice1[0], dice1[1], dice1[2], dice1[3], dice1[4], dice1[5]]
for i in range(6):
    if move(i) == dice2:
        eq = 1
        break
else:
    for j in range(4):
        if move(6) == dice2:
            eq = 1
            break
if not eq:
    print("No")
else:
    print("Yes")

# The refactored version has fewer lines and improved readability. It is now more concise, clear, and easier to understand.