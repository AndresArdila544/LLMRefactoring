```python
while True:
    x = input()
    if int(x) > 0:
        print(sum([int(i) for i in x]))
    else:
        break
```