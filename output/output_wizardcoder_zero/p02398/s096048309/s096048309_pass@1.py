```python
a, b, c = map(int, input().split())
print((b-a+1) - sum(c%i==0 for i in range(max(1, a)))