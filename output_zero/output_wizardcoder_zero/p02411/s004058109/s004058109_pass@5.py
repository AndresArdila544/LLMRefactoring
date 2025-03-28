```python
while True:
    m, f, r = map(int, input().split())
    if (m, f) == (-1, -1):
        break

    s = m + f
    
    if any((s < 30, m == -1 or f == -1, s < 50 and r < 50):
        print('F')
    elif s < 65:
        print('D')
    elif s < 80:
        print('C')
    else:
        print('B')
```