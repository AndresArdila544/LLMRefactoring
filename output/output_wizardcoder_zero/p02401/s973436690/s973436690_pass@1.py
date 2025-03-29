```python
while True:
    try:
        a, op, b = input().split()
        if op == "?":
            break
        elif op in ["+", "-", "*", "/"]:
            print(eval(f"{a}{op}{b}"))
    except ValueError:
        pass
```