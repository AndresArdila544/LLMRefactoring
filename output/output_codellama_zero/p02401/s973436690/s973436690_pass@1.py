```
while True:
    try:
        a, op, b = input().split()
        a, b = int(a), int(b)
        if op == "?":
            break
        elif op == "+":
            print(a+b)
        elif op == "-":
            print(a-b)
        elif op == "*":
            print(a*b)
        elif op == "/":
            print(a//b)
    except ValueError:
        break
```