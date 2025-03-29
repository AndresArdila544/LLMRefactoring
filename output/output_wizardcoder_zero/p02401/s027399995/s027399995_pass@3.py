Here is the refactored version of the code:
```python
while True:
    a, op, b = map(int, input().split())
    if op == '?':
        break
    elif op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        print(a // b)
```