The original code is already concise and readable as it is. Refactoring will only reduce its lines without changing its functionality and readability. Here's a possible refactored version of the program:
```python
a, b = map(int, input().split())
print(f"{a // b}, {float(a) / b :.8f}")  # or print("{:d}, {:.8f}".format(a//b, a/b)) if you prefer to use formatting
```
This version still accomplishes the same thing as the original, but it uses f-strings and integer division (//) to make the code more concise and pythonic.