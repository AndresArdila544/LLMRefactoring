n = int(input())
listA = [list(map(int, input().split())) for _ in range(n)]
building = [[[0] * 10 for _ in range(3) for _ in range(4)] for _ in range(4)]

for building_num, room_details in listA:
    building[building_num-1][floor_num-1][room_num-1] += value

print('\n'.join(' '.join(map(str, floor)) for building in building[:3] for floor in building) + '\n' + '#' * 20)
for building in building[3:]:
    print('\n'.join(' '.join(map(str, floor)) for floor in building) or '') # use empty string instead of None if you want no output for the last 4 buildings.