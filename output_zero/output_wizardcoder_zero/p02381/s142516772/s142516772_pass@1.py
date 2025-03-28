```python
while True:
    try:
        n = int(input())
        if n == 0:
            break
        a = [float(x) for x in input().split()]
        average = sum(a) / n
        print((sum([(i - average) ** 2 for i in a]) / n) ** 0.5)
    except ValueError:
        break 
```