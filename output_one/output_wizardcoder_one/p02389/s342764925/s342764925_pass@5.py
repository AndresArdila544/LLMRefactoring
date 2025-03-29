```python
a, b = input().split()
print(int(a) * int(b), 2*(int(a) + int(b)))
```

This refactored version uses tuple unpacking and no if statement is needed since the condition given in the original code is always true. This is more concise and achieves the same functionality as the original program.
```python
print(int(a) * int(b), 2*(int(a) + int(b)))
```