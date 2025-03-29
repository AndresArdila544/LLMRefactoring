def dice_rotation(dice, command):
    tmp_dice = list(dice)
    #S:1->2,2->6,6->5,5->1
    if command == 'S':
        dice[0], dice[4], dice[5] = tmp_dice[4], tmp_dice[5], tmp_dice[1]
    #N:1->5,5->6,6->2,2->1
    elif command == 'N':
        dice[0], dice[1], dice[5] = tmp_dice[1], tmp_dice[5], tmp_dice[4]
    #W:1->4,4->6,6->3,3->1
    elif command == 'W':
        dice[0], dice[2], dice[5] = tmp_dice[2], tmp_dice[5], tmp_dice[3]
    #E:1->3,3->6,6->4,4->1
    else:
        dice[0], dice[3], dice[5] = tmp_dice[3], tmp_dice[5], tmp_dice[2]
    
def dice_spinning(dice):
    global num_rotations
    num_rotations += 1
    for i in range(6):
        tmp_dice = list(dice)
        #rotate dice by shifting the elements
        dice[i] = tmp_dice[(i+2)%6]
        
def comparison_dices(Dice1, Dice2):
    yes_counter = 0
    for i in range(6):
        if Dice1[i] == Dice2[i]:
            yes_counter += 1
    return yes_counter == 6

def full_validation_dices(Dice1, Dice2):
    global num_rotations
    for i in range(4):
        if comparison_dices(Dice1, Dice2):
            return True
        else:
            dice_spinning(Dice2)
        
    num_rotations = 0
    
    for j in range(num_rotations, 8-num_rotations):
        if comparison_dices(Dice1, Dice2):
            return True
        else:
            dice_spinning(Dice2)
        
        #rotate the second dice by 'S' direction
        dice_rotation(Dice2, 'S')
    
    num_rotations = 0
    
    for j in range(4):
        if comparison_dices(Dice1, Dice2):
            return True
        else:
            dice_spinning(Dice2)
        
        #rotate the second dice by 'W' direction
        dice_rotation(Dice2, 'W')
    
    num_rotations = 0
    
    for j in range(num_rotations, 8-num_rotations):
        if comparison_dices(Dice1, Dice2):
            return True
        else:
            dice_spinning(Dice2)
        
        #rotate the second dice by 'E' direction
        dice_rotation(Dice2, 'E')
    
    num_rotations = 0
    
    return False

def test():
    n = int(input())
    Dices = []
    for _ in range(n):
        Dices.append(list(map(int, input().split()))
        
    result = True
    num_rotations = 0
    
    for i in range(n-1):
        for j in range(i+1, n):
            if full_validation_dices(Dices[i], Dices[j]):
                result = False
                break
            
    print("Yes" if result else "No")