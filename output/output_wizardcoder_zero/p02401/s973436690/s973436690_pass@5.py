```python
while True:
    a, op, b = map(int, input().split())
    
    if op == "?":
        break
    else:
        print({"+": lambda x, y: x+y, "-": lambda x, y: x-y, "*": lambda x, y: x*y, "/": lambda x, y: x//y}[op](a, b)
```