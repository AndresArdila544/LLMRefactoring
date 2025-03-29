```python
tate, yoko = map(int, input().split())
print("{:.2f}".format((tate * yoko) + (2*(tate + yoko)) / 2))
```

This refactored version uses string formatting to print the answer in two decimal places instead of calculating and storing `syuu` and then printing it separately. The variable names are also renamed for clarity, making it more concise and easier to read.

Note: `2*(tate + yoko)` can be written as `2 * (tate + yoko)` without any parentheses.