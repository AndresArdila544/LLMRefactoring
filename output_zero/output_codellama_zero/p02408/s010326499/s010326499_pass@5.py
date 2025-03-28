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
        if C[i][j]:
            print("{}{}".format("SHCD"[i], j+1))