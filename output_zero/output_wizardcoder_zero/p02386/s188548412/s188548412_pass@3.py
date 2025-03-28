def dice_rotation(dice, command):
    tmp = [0] * 6
    for i in range(6):
        tmp[i], dice[(i + 5) % 6] = dice[(i - (command == 'S') % 6], dice[(i + 1) % 6])
    return dice

def full_validation_dices(Dice1, Dice2):
    judgement_result = False
    for _ in range(4):
        if comparison_dices(Dice1, Dice2):
            return True
        else:
            Dice2 = dice_rotation(Dice2, 'S')
    for _ in range(4):
        if comparison_dices(Dice1, Dice2):
            return True
        else:
            Dice2 = dice_rotation(Dice2, 'W')
    return False

def test():
    n = int(input())
    Dices = [list(map(int, input().split())) for _ in range(n)]
    result = all(full_validation_dices(Dices[i], Dices[j]) for i in range(n) for j in range(i + 1, n))
    print('Yes' if result else 'No')

if __name__ == "__main__":
    test()