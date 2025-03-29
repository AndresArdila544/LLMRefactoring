n, m, l = map(int, input().split())
mat_a = [list(map(int, input().split())) for _ in range(n)]
mat_b = [list(map(int, input().split()) for _ in range(m)]
ans = 0
for i in mat_a:
    row_sum = sum(i[j] * mat_b[j][l-1] for j in range(len(mat_b))
    print(' '.join(str(row_sum) for _ in range(l))