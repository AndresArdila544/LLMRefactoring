```python
n = int(input())
A = list(map(str, input().strip().split()))[::-1]
print(" ".join(A))