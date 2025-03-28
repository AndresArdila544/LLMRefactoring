input_data = input().split(" ")
items = [int(cont) for cont in input_data]
dice = dict(zip(["T", "S", "E", "W", "N", "B"], items))

def rot_func(rot, dice):
    if rot == "N":
        new_dice = {"T": dice['S'], "S": dice['B'], "B": dice['N'], "N": dice['T']}
    elif rot == "S":
        new_dice = {"T": dice['N'], "S": dice['T'], "B": dice['E'], "N": dice['W']}
    elif rot == "E":
        new_dice = {"T": dice['W'], "S": dice['T'], "B": dice['B'], "N": dice['E']}
    else:  # rot == "W"
        new_dice = {"T": dice['E'], "S": dice['B'], "B": dice['W'], "N": dice['T']}
    return new_dice

def search(conds, dice):
    a, b = conds
    a_key = [k for k, v in dice.items() if v == a]
    b_key = [k for k, v in dice.items() if v == b]
    key_list = a_key + b_key
    part_st = ''.join(key_list)
    def search(part_st):
        if part_st in "TNBST":
            return "W"
        elif part_st in "TSBNT":
            return "E"
        elif part_st in "TEBWT":
            return "N"
        elif part_st in "TWBET":
            return "S"
        elif part_st in "NESWN":
            return "B"
        else:  # part_st in "NWSEN"
            return "T"
    target_key = search(part_st)
    return dice[target_key]

repeater = int(input())
for neee in range(repeater):
    control_input = input().split(" ")
    conds = [int(i) for i in control_input]
    dice = rot_func(*conds, dice=dice)
    print(search(conds, dice))