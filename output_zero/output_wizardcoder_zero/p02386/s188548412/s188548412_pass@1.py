def rotate_dice(dice):
    return [dice[4], dice[5], dice[0], dice[1], dice[2], dice[3]]


def compare_dices(Dice1, Dice2):
    yes_counter = 0
    for j in range(6):
        if Dice1[j] == Dice2[j]:
            yes_counter += 1
    return yes_counter == 6

def validate_dices(Dice1, Dice2):
    judgement_result = False
    for i in range(4):
        if compare_dices(Dice1, Dice2) or compare_dices(rotate_dice(Dice1), rotate_dice(Dice2)):
            return True
        else:
            rotate_dice(Dice2)
    for i in range(4):
        if compare_dices(Dice1, Dice2) or compare_dices(rotate_dice(Dice1), rotate_dice(Dice2)):
            return True
        else:
            rotate_dice(Dice2)
    return False

def test():
    n = int(input())
    
    for _ in range(n-1):
        Dices = [list(map(int, input().split())) for i in range(n)]
        
        for i in range(n-1):
            for j in range(i+1, n):
                if validate_dices(Dices[i], Dices[j]):
                    print("Yes")
                    return
    
    print("No")