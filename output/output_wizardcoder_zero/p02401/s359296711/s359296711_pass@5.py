```python
while True:
    a, op, b = map(str, input().split())
    c = int(a)
    d = int(b)
    if op == '+': result = c + d
    elif op == '-': result = c - d
    elif op == '*': result = c * d
    elif op == '/': result = int(c / d)  # cast to integer, otherwise the result will be float and won't work with print()
    else: break
    print("{0}".format(result))
```