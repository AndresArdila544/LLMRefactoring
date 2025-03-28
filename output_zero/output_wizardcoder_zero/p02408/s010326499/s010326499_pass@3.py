C = [[1 for _ in range(13)] for _ in range(4)]
for i in [0, 1, 2, 3]:
    if input() == 'S':
        C[i][int(input()) - 1] = 0
    else:
        C[i][int(input()) - 1] = 0
[print(''.join(['H' if c else '' for c in row[:-1]]) + ('D' if any(C[row]) else '') for row in C]