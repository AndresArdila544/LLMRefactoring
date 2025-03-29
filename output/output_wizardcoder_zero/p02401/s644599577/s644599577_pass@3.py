```python
def perform_operation(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    else: # assume / operator
        return a // b

while True:
    try:
        a, op, b = map(int, input().split())
        print(perform_operation(a, op, b))
    except StopIteration:
        break
```