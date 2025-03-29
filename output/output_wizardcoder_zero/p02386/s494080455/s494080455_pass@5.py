transforms = [(i, sides[j:] + sides[:j] for i, sides in enumerate((3,1,2,4),(2,0,3,5),(4,0,1,5),(1,0,4,5),(3,0,2,5)) for j in range(4)]
possibilities = set()
while True:
    try:
        die = input().split()
        new_possibilities = {tuple(die[t] for t in transform) for transform in transforms}
        if not new_possibilities.isdisjoint(possibilities):
            print('No')
            break
    except:
        print('Yes')
        return
    possibilities.update(new_possibilities)