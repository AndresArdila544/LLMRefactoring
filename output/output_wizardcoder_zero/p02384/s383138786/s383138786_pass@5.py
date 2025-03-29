```python
def rot_func(rot, dice):
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
    return dice

def search_surf(conds):
    a, b = conds
    a_key = [k for k, v in dice.items() if v == a]
    b_key = [k for k, v in dice.items() if v == b]
    key_list = a_key + b_key
    
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
        elif part_st in "NWSEN":
            return "T"
    
    target_key = search(''.join(key_list))
    print(dice[target_key])
    
input_data = input().split(" ")  # input_data = [1,2,3,4]
items = [int(cont) for cont in input_data]
keys = ['T', 'S', 'E', 'W', 'N', 'B']
dice = dict(zip(keys, items))  # dice = {'T':1, 'S':2, 'E':3, 'W':4}

for i in input():  # controls = ['N','S', 'E', ...]
    rot_func(i, dice)
print(dice['T'])

a = input()  # repeater = 2
for neee in range(repeater):
    control_input = input().split(" ")  # conds = [1,2] or [3,4]
    search_surf([int(i) for i in control_input])
```