```python
x = input()
while True:
    try:
        x_list = [int(i) for i in str(x)]
        print(sum(map(int, x))
        break if int(x) <= 0 else continue
    except ValueError:
        pass
```