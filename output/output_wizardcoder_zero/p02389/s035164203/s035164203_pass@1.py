```python
x, y = map(int, input().split())
print("{0} {1}".format(2*x+y, 2*(x+y))
```

This is a more concise and cleaner version of the original code. It uses string formatting to avoid having to call `print()` twice and concatenate strings. Note that I also removed the unnecessary parentheses around the `split()` function call since they are not needed when using `map()` with `int()`.