Here's a more concise version of the program that still achieves the same functionality as the original one:

```python
x, y = map(int, input().split())
print(f"{2 * (x + y)} {2 * (x * y)}")  # Using f-strings to format output and reduce curly braces
```

This version has the same functionality as the original program, but it's less verbose and easier to read. Instead of printing the variables separately, we can combine them into a single string using an f-string and multiplying the x and y values accordingly.