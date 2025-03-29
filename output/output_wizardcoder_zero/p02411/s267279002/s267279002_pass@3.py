```python
while True:
    m, f, r = map(int, input().split())
    if m == -1 and f == -1:
        break
    elif m > 0 and f > 0 and (m + f) >= 80:
        print('A')
    elif m > 0 and f > 0 and (m + f) >= 65:
        print('B')
    elif m > 0 and f > 0 and (m + f) >= 50:
        if r >= 50:
            print('C')
        else:
            print('D')
    else:
        print('F')
```