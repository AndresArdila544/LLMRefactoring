```python
while True:
    m, f, r = map(int, input().split())
    if (m == f == r) == -1:
        break
    elif m != -1 and f != -1 and 30 <= m + f < 50:
        print("D")
    elif m + f >= 50 and r >= 50:
        print("C")
    elif 29 <= m + f < 80:
        print("B")
    else:
        print("A")
```