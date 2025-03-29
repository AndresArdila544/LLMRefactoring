```python
a = int(input().rstrip())
b = int(input().split()[1])
print("a > b" if a > b else "a < b" if a < b else "a == b")