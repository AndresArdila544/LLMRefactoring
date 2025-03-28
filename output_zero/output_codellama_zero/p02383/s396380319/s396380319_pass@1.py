move = input().split()
dice = [int(x) for x in input().split()]
dire = {"N":[2,6,3,4,1,5],"S":[5,1,3,4,6,2],"E":[4,2,1,6,5,3],"W":[3,2,6,1,5,4]}
em = []
for i in range(len(move)):
    em = dice[:]
    for j in range(len(dice)):
        em[j] = dice[dire[move[i]][j]-1]
    else:
        del dice[:]
        dice.extend(em)
print(dice[0])