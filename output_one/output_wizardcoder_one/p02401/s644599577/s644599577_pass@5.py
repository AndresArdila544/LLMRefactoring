```python
a, op, b = map(int, input().split())
while True:
    if op == "?":
        break
    a, op, b = int(input()), input(), int(input())
    ans = { "+": lambda x, y: x+y, "-": lambda x, y: x-y, "*": lambda x, y: x*y, "/": lambda x, y: x//y }[op](a, b)
    print("{}".format(ans))
```