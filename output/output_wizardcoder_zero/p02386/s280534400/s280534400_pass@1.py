def roll(dice, d):
    if   d == "N": dice[0], dice[1] = dice[1], dice[5]; dice[4], dice[5] = dice[4], dice[0]
    elif d == "S": dice[0], dice[4] = dice[4], dice[5]; dice[4], dice[1] = dice[0], dice[4]
    elif d == "W": dice[3], dice[0] = dice[0], dice[2]; dice[2], dice[5] = dice[5], dice[0]
    else: dice[3], dice[5] = dice[3], dice[0]; dice[0], dice[2] = dice[5], dice[3]

def same_dice(D1, D2):
    return all(roll(D1.num, d) == roll(D2.num, d) for d in buff)

buff = "NNNNWNNNWNENNN" # Assuming that the input string is valid and correct
N = int(input())
dices = [Dice([int(i) for i in input().split()] if N > 0 else range(6)] * N
for i in range(N):
    for j in range(i + 1, N):
        if same_dice(dices[i], dices[j]):
            print("No")
            break # exit the inner loop as soon as a pair is found
    else: # executed if no "break" was encountered (if the for loop completed without finding a match)
        continue # move on to next outer loop iteration
else: # executed if all loops complete without encountering a "break"
    print("Yes")