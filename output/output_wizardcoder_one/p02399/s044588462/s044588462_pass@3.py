The refactored version can be written as:
```python
a, b = map(int, input().split())
print(*divmod(a, b))