```python
a, b = map(int, input().split())
print(*[f"{d // b} {d % b} {d / b}" for d in [a]])
```