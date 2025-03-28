```python
a, b = map(int, input().split())
print("a", "<" if a < b else "a" if a == b else ">", "b")