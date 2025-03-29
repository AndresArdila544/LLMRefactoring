```python
import math
n, m, l = map(int, input().split())
A = [[0 for _ in range(m)] for _ in range(n)]
B = [[0 for _ in range(l)] for _ in range(m)]
C = [[0 for _ in range(l)] for _ in range(n)]
for row, arow in zip(range(n), [list(map(int, input().split()) for _ in range(m)]):
    A[row] = arow
for row, brow in zip(range(m), [list(map(int, input().split()) for _ in range(m)]:
    B[row] = brow
for i, j in ((i,j) for i in range(n) for j in range(l)):
    C[i][j] = sum(A[i][k]*B[k][j] for k in range(m))
for row in range(n):
    print(*C[row])
```