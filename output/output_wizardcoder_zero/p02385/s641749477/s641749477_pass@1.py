def roll_dice(dice):
    directions = {'S': (4,0,2,3,5,1), 'N': (1,5,2,3,0,4), 'E': (3,1,0,5,4,2), 'W': (2,1,5,0,4,3), 'Y': (0,3,1,4,2,5)}
    dice.a = [dice.t, dice.f, dice.r, dice.l, dice.b, dice.u]
    
    for roll in s:
        dice_copy = Dice(*[int(x) for x in input().split()])
        
        if dice.a == dice_copy.a:
            ans = 'Yes'
            break
        
        dice_copy.roll(directions[roll])
    else:
        dice_copy.roll(w)
    
    print(ans)

s, w = 'SSSEWW', 'YYYY'
dice1 = Dice(*map(int, input().split()))
dice2 = Dice(*map(int, input().split())

roll_dice(dice1)