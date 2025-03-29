```python
while True:
    n = input()
    if not n:
        break
    x, y = map(int, n.split())
    if x > y:
        print(y, ' ', x)
    else:
        print(n)
```