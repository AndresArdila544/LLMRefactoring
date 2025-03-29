n, m, l = map(int, input().split())
YEH, FUK = [list(map(int,input().split()) for i in range(n)), [list(map(int,input().split()) for j in range(m)]
for _ in range(l):
    GOMI = 0
    for i in range(n):
        for k in range(m):
            GOMI += FUK[i][k]*YEH[k]
    print(*FUK)
print()