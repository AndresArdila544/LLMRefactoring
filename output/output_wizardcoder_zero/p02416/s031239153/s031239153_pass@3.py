```python
while True:
    try:
        x = input()
        if x == '0':
            break
        else:
            print(sum(map(int, x))
    except ValueError:
        pass
```