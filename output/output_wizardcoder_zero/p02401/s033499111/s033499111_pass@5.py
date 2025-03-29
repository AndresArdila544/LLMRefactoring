```python
while True:
    a, op, b = map(int, input().split())
    if op == "+":
        print(a+b)
    elif op == "-":
        print(a-b)
    elif op == "*":
        print(a*b)
    elif op == "/":
        print(a/b)
    else: # assuming the only other valid operator is "?" to break out of loop
        break
```