while True:
    input_str = input()
    if input_str == '0': break
    print(sum(map(int, input_str))
```python
while True:
    try:
        n = int(input())
        if n == 0:
            break
        else:
            print(sum(list(map(int, str(n))))
    except ValueError:
        pass
```