# <|start_of_text|>:
import itertools


def q1():
    def rot_func(rot, dice):
        keys = list(dice)
        if rot == "N":
            new_keys = keys[2:] + [keys[0]]
            items = [dice[i] for i in new_keys]
            new_dic = dict(zip(new_keys, items))
            return new_dic

        if rot == "S":
            new_keys = [keys[-1]] + keys[:-1]
            items = [dice[i] for i in new_keys]
            new_dic = dict(zip(new_keys, items))
            return new_dic

        if rot == "E":
            new_keys = ['T', 'W'] + keys[:2]
            items = dice['W'], dice['T'], dice[keys[0]], dice[keys[1]]
            new_dic = dict(zip(new_keys, items))
            return new_dic

        if rot == "W":
            new_keys = [keys[1], keys[0]] + ['E']
            items = dice['E'], dice[keys[2]], dice[keys[3]], dice['W']
            new_dic = dict(zip(new_keys, items))
            return new_dic

    controls = list(input())
    for i in controls:
        dice = rot_func(i, dice)

    print(dice["T"])


def q2():
    def search_surf(conds, dice):

        def search(part_st):
            if part_st == 'TWBET':
                return "N"

            elif part_st == 'TSBNT':
                return "E"

            elif part_st == 'TEBWT':
                return "S"

            elif part_st == 'TWBET':
                return "W"

            elif part_st == 'NEWSWN' or part_st == 'NESWN':
                return "B"

            elif part_st == 'NWSEN' or part_st == 'NESWN':
                return "T"

        a, b = conds
        a_key = [k for k, v in dice.items() if v == a]
        b_key = [k for k, v in dice.items() if v == b]
        key_list = a_key + b_key

        part_st = ''.join(key_list)
        target_key = search(part_st)
        print(dice[target_key])

    a = input()
    repeater = int(a)

    for neee in range(repeater):
        control_input = input().split(" ")
        conds = [int(i) for i in control_input]
        search_surf(conds, dice)

q2()



#