```python
a, b = map(int, input().split())
print(f"{a * b}, {2 * (a + b)}")  # noqa: WPS432
```

Explanation:
- `input().split()` splits the input string on whitespace and returns a list of strings.
- `map(int, ...)` applies the `int` function to each element of that list to convert it from a string representation of an integer into an actual integer object.
- The expression `a * b` multiplies the two integers together. We use parentheses for clarity.
- The expression `(a + b)` adds the two integers together, and we use parentheses for clarity as well.
- We can concatenate strings using commas in a formatted string literal, so `"{}, {}".format(x, y)` is equivalent to `str(x) + ", " + str(y)`.