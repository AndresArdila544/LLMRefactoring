```python
a, b = map(int, input().split())
print(*map(str, (a // b, a % b, a / b))  # Using * to unpack and print all values in the tuple.
```