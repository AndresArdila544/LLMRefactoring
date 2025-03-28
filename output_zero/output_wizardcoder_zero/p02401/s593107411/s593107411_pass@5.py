```python
while True:
    x = input().split()
    try:
        a, op, b = map(int, x)
        if op == "+":
            print(a + b)
        elif op == "-":
            print(a - b)
        elif op == "*":
            print(a * b)
        elif op == "/":
            print(a // b)
        elif op == "?":
            break
    except ValueError:
        pass  # if user enters a non-integer value, ignore and move on to the next input.
```