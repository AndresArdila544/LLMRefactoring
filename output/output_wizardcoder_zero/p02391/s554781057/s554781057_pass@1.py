```python
a, b = map(int, input().split())
print('{} {} {}'.format("a" if a < b else "=" if a == b else ">", "b")
```