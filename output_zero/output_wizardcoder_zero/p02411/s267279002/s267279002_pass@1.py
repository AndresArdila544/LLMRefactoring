```python
while True:
    m, f, r = map(int, input().split())
    if m == -1 and f == -1:
        break
    elif m >= 80 or f >= 80:
        print('A')
    elif (m + f) >= 70:
        print('B')
    elif (m + f) >= 50 and r >= 50:
        print('C')
    else:
        print('F')
```