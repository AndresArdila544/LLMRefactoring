def roll_dice(dice):
    work = dice[:]  # make a copy of the dice's number list
    order = 'NNNNWNNNWNNNENNNENNNWNNN'
    for i in range(6):
        if order[i] == 'E':
            dice[3], dice[1], dice[0], dice[5], dice[4], dice[2] = work[3], work[1], work[0], work[5], work[4]
        elif order[i] == 'N':
            dice[1], dice[5], dice[2], dice[3], dice[0], dice[4] = work[1], work[5], work[2], work[3], work[0]
        elif order[i] == 'S':
            dice[4], dice[0], dice[2], dice[3], dice[5], dice[1] = work[4], work[0], work[2], work[3], work[5]
    return dice

def compare_dice(diceA, diceB):
    for i in range(6):
        if diceA[i] != diceB[i]:
            return False
    return True

tableA = list(map(int, input().split()))
tableB = list(map(int, input().split()))
diceA = roll_dice([*tableA])  # unpack the list into arguments for the new dice class
diceB = [*tableB]        # unpack the list into arguments for the new dice class

if compare_dice(diceA, diceB):
    print("Yes")
else:
    print("No")