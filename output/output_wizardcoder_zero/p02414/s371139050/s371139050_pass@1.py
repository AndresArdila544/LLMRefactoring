n, m, l = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split()) for _ in range(m))
C = [[0]*l for _ in range(n)]
for i in range(n):
    C[i] = sum(a * b for a, b in zip(A[i], (B[:, j])) for j in range(l) if j < m)

for c in C:
    print(*c)