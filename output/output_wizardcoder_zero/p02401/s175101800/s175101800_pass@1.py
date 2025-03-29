```python
def perform_operation(a, b, operator):
    if operator == '+':
        return int(a) + int(b)
    elif operator == '-':
        return int(a) - int(b)
    elif operator == '*':
        return int(a) * int(b)
    elif operator == '/':
        return int(int(a) / int(b))

while True:
    a, op, b = input().split()
    if op == '?':
        break
    else:
        print(perform_operation(a, b, op))
```