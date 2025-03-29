```python
a, op, b = map(int, input().split())
while True:
    if op == "?":
        break
    else:
        a_op_b = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x // y
        }[op]
        ans = a_op_b(a, b)
        print("{}".format(ans))
        a, op, b = map(int, input().split())
```