```python
matrix_size = list(map(int, input().split()))
vector_b = list(map(int, input().split()))
result = [[x*y for x, y in zip(*mtrx)] for mtrx in [list(zip(*matrix)]] for y in vector_b]
print(*result)
```