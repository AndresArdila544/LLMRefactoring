```python
while True:
    try:
        a, op, b = map(str, input().split())
        c = int(a)
        d = int(b)
        print("{0}".format({'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: int(x / y)}.get(op)(c, d))
    except (ValueError, ZeroDivisionError):
        print('Invalid input')
    except KeyError:
        break
```