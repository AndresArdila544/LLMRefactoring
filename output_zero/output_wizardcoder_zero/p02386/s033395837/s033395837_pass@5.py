num = int(input())
for n in range(num):
    dice_[n] = [int(i) for i in input().split()]
dice[n] = {(0,0,1):dice_[n][0], (0,-1,0):dice_[n][1], (1,0,0):dice_[n][2], (-1,0,0):dice_[n][3], (0,1,0):dice_[n][4], (0,0,-1):dice_[n][5]}
for n in range(num):
    dice_keys = [i for i in dice[n].keys()]
    varif_child = [1*dice[n][min_] + 10*dice[n][on] + 100*dice[n][tw] + 1000*dice[n][th] + 10000*dice[n][fo] + 10000*dice[n][opposing] for on, tw, th, fo in [(i, cross(min_, i), cross(min_, cross(min_, i))) for min_ in dice_keys] for opposing in [tuple([-i for i in min_])] if opposing not in dice_keys[:n]]
    varif[n] = min(varif_child)
print("Yes" if len(set(varif)) == num else "No")