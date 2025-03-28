n, m, l = map(int, input().split())
mat_a = []
mat_b = []
for i in range(n):
    array = list(map(int, input().split()))
    mat_a.append(array)
for i in range(m):
    array = list(map(int, input().split()))
    mat_b.append(array)
ans = 0
for i in range(n):
    for k in range(l):
        ans += sum([mat_a[i][j] * mat_b[j][k] for j in range(m)])
        print('{}' .format(ans), end='') if k != 0 else print(ans, end='')
    print()