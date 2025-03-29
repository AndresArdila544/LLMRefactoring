```python
N, M, L = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
B = [list(map(int, input().split()) for _ in range(M)
for i in range(N):
    C[i] = ' '.join(str(sum(A[i][k]*B[k][j] for k in range(M)) for j in range(L))
for row in C:
    print(*row.split())
```