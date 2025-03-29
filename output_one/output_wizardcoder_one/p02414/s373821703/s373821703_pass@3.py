n, m, l = map(int, input().split())
YEAH = [list(map(int, input().split())) for i in range(n)]
FUCK = [list(map(int, input().split()) for i in range(m) for j in range(l)]
for i in range(n):
    for j in range(l-1):
        GOMI = 0
        for k in range(m):
            GOMI += FUCK[k][j] * YEAH[i][k]
        print(GOMI, end=" ")
    print(sum(FUCK[k][l-1]*YEAH[i][k] for k in range(m))