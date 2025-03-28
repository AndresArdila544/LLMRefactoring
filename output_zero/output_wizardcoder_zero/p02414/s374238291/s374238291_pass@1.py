n, m, l = map(int, input().split())
mat_a = [list(map(int, input().split())) for _ in range(n)]
mat_b = [list(map(int, input().split()) for _ in range(m)]
ans = 0
for i in range(n):
    for j in range(l):
        for k in range(m):
            ans += mat_a[i][j] * mat_b[j][k]
            if k != l-1: print(' ', end='')
        print(ans, end='\n')