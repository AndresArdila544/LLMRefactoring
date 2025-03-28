def q1():
    dice = {'T': int(input()), 'S': int(input()), 'E': int(input()), 'W': int(input()), 'B': int(input())}
    rotations = {'N': ['T', 'S', 'B', 'N'], 'S': ['T', 'S', 'B', 'N'], 'E': ['T', 'E', 'B', 'W'], 'W': ['T', 'E', 'B', 'W']}
    controls = input().split()
    for rot in controls:
        dice = dict(zip(rotations[rot], [dice['S'], dice['B'], dice['N'], dice['T'] if rot != 'N' else dice['T'], dice['E'] if rot != 'W' else dice['T'], dice['W'] if rot != 'N' else dice['B']]))
    print(dice['T'])

def q2():
    def search_surf(conds):
        a, b = conds
        common_keys = []
        for k in ['T', 'S', 'W', 'E', 'B']:
            if k in [str(a), str(b)]:
                common_keys.append(k)
        target_key = ''.join(common_keys)
        
        def search(target_key):
            if target_key == "TW":
                return "S"
            elif target_key == "TSN":
                return "E"
            elif target_key in ["TE", "BW"]:
                return "N"
            else:
                return "T"
        
        for _ in range(int(input())):
            conds = [int(i) for i in input().split()]
            common_keys = []
            for k in ['T', 'S', 'W', 'E', 'B']:
                if k in map(str, conds):
                    common_keys.append(k)
            target_key = ''.join(common_keys)
            print(dice[search(target_key))

q1()
q2()