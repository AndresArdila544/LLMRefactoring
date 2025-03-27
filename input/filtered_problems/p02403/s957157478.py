sides = list(map(int, input().split()))
while sides != [0, 0]:
    line = '#' * sides[1] + '\n'
    lines = line * sides[0]
    print(lines)
    sides = list(map(int, input().split()))
