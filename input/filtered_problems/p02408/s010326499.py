C = []
for _ in range(4):
    c = [i for i in range(1, 14)]
    C.append(c)
n = int(input())
for _ in range(n):
    i, j = map(str, input().split())
    j = int(j)
    if i == 'S':
        C[0][j - 1] = 0
    elif i == 'H':
        C[1][j - 1] = 0
    elif i == 'C':
        C[2][j - 1] = 0
    else:
        C[3][j - 1] = 0
for i in range(4):
    for j in range(13):
        if C[i][j] != 0:
            if i == 0:
                print('S', end=' ')
                print(j + 1)
            elif i == 1:
                print('H', end=' ')
                print(j + 1)
            elif i == 2:
                print('C', end=' ')
                print(j + 1)
            else:
                print('D', end=' ')
                print(j + 1)
