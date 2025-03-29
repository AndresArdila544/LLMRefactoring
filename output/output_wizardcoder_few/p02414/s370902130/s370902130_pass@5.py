```python
n, m, l = map(int, input().split())

A = [[0 for _ in range(m)] for _ in range(n)]
B = [[0 for _ in range(l)] for _ in range(m)]
C = [[0 for _ in range(l)] for _ in range(n)]

for i, row in enumerate(map(lambda x: list(map(int, input().split())[:m], range(n)):
    A[i] = list(row)

for j, brow in enumerate(map(lambda x: list(map(int, input().split()), range(m):
    B[j] = list(brow)

for i in range(n):
    for j in range(l):
        C[i][j] = sum([A[i][k]*B[k][j] for k in range(m)]

for row in zip(*C):
    print(' '.join(map(str, row))
```