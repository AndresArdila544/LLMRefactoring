```python
a, b = map(int, input().split())
print((b-a+1) - sum([i % c == 0 for i in range(a, b+1)])
```