refactored_dice = [int(x) for x in input().split()]
move = input()
dice = []
for i in range(len(move)):
    dice = refactored_dice[:]
    for j in range(len(dice)):
        dice[j] = refactored_dice[["NESW".index(move[i])]-1]
    else:
        del refactored_dice[:]
        refactored_dice.extend(dice)
print(refactored_dice[0])