def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])

num = int(input())
dice_ = [int(input().split()) for _ in range(num)]
dices = {}
varif = []
for n in range(num):
    dices[n] = {(0, 0, 1): dice_[n][0], (0, -1, 0): dice_[n][1], (1, 0, 0): dice_[n][2], (-1, 0, 0): dice_[n][3], (0, 1, 0): dice_[n][4], (0, 0, -1): dice_[n][5]}
    varif.append(min([dices[n][k] + 10 * dices[n][(-i, j, k) if i != j else 0] + 100 * dices[n][(j, -i, k] if j != k else 0] for (i, j, k) in [(0, 1, 2), (-1, 0, 0), (1, 0, 1), (0, 1, -1), (0, 0, -1)]]))
if len(set(varif)) == num:
    print("Yes")
else:
    print("No")