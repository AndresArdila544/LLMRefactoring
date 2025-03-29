```
while True:
    a, op, b = input().split()
    a = int(a)
    b = int(b)
    if op == '?':
        break
    else:
        print({"+": a + b, "-": a - b, "*": a * b, "/": a // b}[op])
```