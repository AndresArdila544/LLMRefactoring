```python
n, m, l = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(m)]
C = [[0]*l for _ in range(n)]
for i in range(n):
    C[i] = sum([A[i][k] * B[k][j] for k in range(m)])
print(*zip(*C))
```