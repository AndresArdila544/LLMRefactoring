dice = list(map(int, input().split()))
move = [*input()]
dire = {"N": [2,6,3,4,1], "S":[5,1,3,4,6], "E":[4,2,1,6,5],"W":[3,2,6,1]}
em = []
for i in range(len(move)):
    em = dice.copy()
    for j in range(len(dice)):
        dice[j] = em[dire[move[i].upper()][j]-1]
print(dice[0])