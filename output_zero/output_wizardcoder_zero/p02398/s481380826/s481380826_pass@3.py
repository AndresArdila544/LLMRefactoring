```python
a, b = map(int, input().split())
print(sum(i % c == 0 for i in range(a, b+1))  # sum counts the number of times an element is true in a generator expression.
```