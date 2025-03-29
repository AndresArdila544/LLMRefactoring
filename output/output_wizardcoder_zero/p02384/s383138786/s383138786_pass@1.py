input_data = input().split(" ")
items = [int(cont) for cont in input_data]
keys = ['T', 'S', 'E', 'W', 'N', 'B']
dice = dict(zip(keys, items))

def rotate_dict(rot, dice):
    if rot == "N":
        new_keys = ['T', 'S', 'N']
        new_items = [dice['S'], dice['B'], dice['N'], dice['T']]
        dice.update(zip(new_keys, new_items))
    
    if rot == "S":
        new_keys = ['T', 'S', 'N']
        new_items = [dice['N'], dice['T'], dice['S'], dice['B']]
        dice.update(zip(new_keys, new_items))
    
    if rot == "E":
        new_keys = ['T', 'E', 'W']
        new_items = [dice['W'], dice['T'], dice['B']]
        dice.update(zip(new_keys, new_items))
    
    if rot == "W":
        new_keys = ['T', 'E', 'W']
        new_items = [dice['E'], dice['B'], dice['W'], dice['T']]
        dice.update(zip(new_keys, new_items))

controls = input().split()
for i in controls:
    rotate_dict(i, dice)
print(dice["T"])

def search_surface(conds, dice):
    a, b = conds
    a_key = [k for k, v in dice.items() if v == a]
    b_key = [k for k, v in dice.items() if v == b]
    key_list = a_key + b_key
    
    def get_surface(part_st):
        if "T" in part_st:
            return "W"
        elif "S" in part_st or "N" in part_st:
            return "E"
        elif "E" in part_st:
            return "N"
        else:
            return "S"
    
    target_key = get_surface(''.join(key_list))
    print(dice[target_key])

a = input()
repeater = int(a)
for _ in range(repeater):
    control_input = [int(i) for i in input().split(" ")]
    search_surface(control_input, dice)