Here is a refactored version of the code:

import sys
write=sys.stdout.write

buildings = [[[], [], []], [[], [], []], [[], [], []], [[], [], []]]
for i in range(4):
    for j in range(3):
        for k in range(10):
            buildings[i][j].append(0)

informations = int(input())

for _ in range(informations):
    information = input().split()
    buildings[int(information[0]) - 1][int(information[1]) - 1][int(information[2]) - 1] += int(information[3])

for i in range(4):
    for j in range(3):
        for k in range(10):
            write(str(buildings[i][j][k]))
            if k < 9:
                write(' ')
            else:
                print()
    if i != 3:
        for _ in range(20):
            write('#')
        print()