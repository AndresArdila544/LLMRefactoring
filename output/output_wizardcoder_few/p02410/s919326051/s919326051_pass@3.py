Here's the refactored version of the given code:

```python
n, m = map(int, input().split())
A = [list(map(int, input().split()) for i in range(n))
B = list(map(int, input().split()) for _ in range(m)
for i in range(n):
    value = sum(A[i][j] * B[j] for j in range(m))
    print(value)
```