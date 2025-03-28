input_data = input().split(" ")
dice = {
    'T': int(input_data[0]),
    'S': int(input_data[1]),
    'E': int(input_data[2]),
    'W': int(input_data[3]),
    'N': int(input_data[4]),
    'B': int(input_data[5])
}

def rot_func_list(rot, dice):
    if rot == "N":
        keys = ['T', 'S', 'B', 'N']
        items = dice['S'], dice['B'], dice['N'], dice['T']
        new_dice = dict(zip(keys, items))
        dice.update(new_dice)
    elif rot == "S":
        keys = ['T', 'S', 'B', 'N']
        items = dice['N'], dice['T'], dice['S'], dice['B']
        new_dice = dict(zip(keys, items))
        dice.update(new_dice)
    elif rot == "E":
        keys = ['T', 'E', 'B', 'W']
        items = dice['W'], dice['T'], dice['E'], dice['B']
        new_dice = dict(zip(keys, items))
        dice.update(new_dice)
    elif rot == "W":
        keys = ['T', 'E', 'B', 'W']
        items = dice['E'], dice['B'], dice['W'], dice['T']
        new_dice = dict(zip(keys, items))
        dice.update(new_dice)

def search_surf(conds, dice):
    a,b=conds
    a_key = [k for k, v in dice.items() if v == a ]
    b_key = [k for k, v in dice.items() if v == b ]
    key_list = a_key + b_key

    part_st = ''.join(key_list)

    def search(part_st):
        if part_st in "TNBST":
            return "W"
        if part_st in "TSBNT":
            return "E"
        if part_st in "TEBWT":
            return "N"
        if part_st in "TWBET":
            return "S"
        if part_st in "NESWN":
            return "B"
        if part_st in "NWSEN":
            return "T"
    target_key = search(part_st)
    print(dice[target_key])

a = input()
repeater = int(a)
for neee in range(repeater):
    control_input = input().split(" ")
    conds = [int(i) for i in control_input]
    search_surf(conds, dice)