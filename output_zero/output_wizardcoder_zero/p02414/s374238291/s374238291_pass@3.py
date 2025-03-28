n, m, l = map(int, input().split())
mat_a = [[int(i) for i in input().split()] for _ in range(n)]
mat_b = [[int(j) for j in input().split()] for _ in range(m)]
ans = 0
for i in mat_a:
    ans += sum(map(lambda x, y: x * y, i, mat_b[k % m])
    if k != 0 and (k+1) % l == 0: print(ans, end='')
    ans = 0
print()
for _ in range(l): print("")