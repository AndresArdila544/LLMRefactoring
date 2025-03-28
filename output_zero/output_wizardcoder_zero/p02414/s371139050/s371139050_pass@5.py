n, m, l = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [[0]*l for i in range(m)]
for i in range(n):
    B[i] = list(map(int, input().split()))
C = [[sum(a*b for a, b in zip(A[i], B[j])) for j in range(l)] for i in range(n)]
print(*[" ".join(str(c) for c in C[i]) for i in range(n)])