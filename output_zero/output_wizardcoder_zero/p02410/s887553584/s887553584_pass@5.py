n, m = map(int, input().split())
A = [list(map(int, input().split()) for i in range(n))
b = list(map(int, input().split() for _ in range(m)
for i in range(n):
    print(sum(A[i][j] * b[j] for j in range(m)))