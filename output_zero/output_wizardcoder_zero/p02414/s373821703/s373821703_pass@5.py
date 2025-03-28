n, m, l = map(int, input().split())
YEAH = [list(map(int, input().split())) for i in range(n)]
FUCK = [list(map(int, input().split()) for i in range(m))

for i in range(n):
    GOMI = sum([FUCK[k][j] * YEAH[i][k] for k in range(m)]
    print(' '.join(str(GOMI) if j != l else str(GOMI + ' ') for j in range(l))