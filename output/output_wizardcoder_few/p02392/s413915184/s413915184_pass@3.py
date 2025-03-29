Here's a refactored version of the program that is shorter, cleaner, and more readable than the original:
```python
a, b, c = map(int, input().split())
print('Yes' if min(a,b) < c else 'No')
```