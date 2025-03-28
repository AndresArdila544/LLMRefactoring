```python
def perform_operation(a: int, op: str, b: int) -> None:
    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        print(a // b)
```

while True:
    try:
        a, op, b = map(int, input().split())
        perform_operation(a, str(op), b)
        if op != '?':
            break
    except ValueError:
        print('Invalid Input')