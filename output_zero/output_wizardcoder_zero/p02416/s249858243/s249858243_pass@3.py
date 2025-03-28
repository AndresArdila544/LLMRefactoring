```python
while True:
    moji = str(input())
    if not moji[0] == '0':
        print(sum(int(num) for num in moji))
    else:
        break