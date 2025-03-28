```python
N, M, L = map(int, input().split())
A = [[int(x) for x in input().split()] for i in range(N)]
B = [list(map(int, input().split())) for i in range(M)]
C = [[0]*L for _ in range(N)]
for n in range(N):
    for l in range(L):
        C[n] = sum([A[n][m]*B[m][l] for m in range(M)])
for row in C:
    print(*row)
```