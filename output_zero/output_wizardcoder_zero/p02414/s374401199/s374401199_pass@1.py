n, m, l = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split()) for _ in range(m)]
C = [[sum(a[k] * b[j] for k in range(l)) for j in range(m)] for a in A]
for line in C:
    print(*line)