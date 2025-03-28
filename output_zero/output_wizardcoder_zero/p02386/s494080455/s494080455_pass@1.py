transforms = [(i, sides[j:], sides[:j]) for i, sides in enumerate(((3,1,2,4),(2,0,3,5),(4,0,1,5),(1,0,4,5),(3,0,2,5)) for j in range(4)]
possibilities = set()
while True:
    dice_str = input().split()
    new_dice = {tuple(dice[t] for t in transform) for dice in transforms}
    if new_dice.intersection(possibilities):
        print('No')
        break
    possibilities.update(new_dice)
else:
    print('Yes')