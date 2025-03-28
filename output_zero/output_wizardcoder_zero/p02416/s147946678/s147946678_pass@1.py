```python
while True:
    x = input()
    if x == '0':
        break
    else:
        print(sum([int(_) for _ in x]))
```