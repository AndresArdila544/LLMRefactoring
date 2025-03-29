```python
while True:
    m, f, r = map(int, input().split())
    if m == f == r == -1:
        break
    
    if m < 0 or f < 0:
        result.append("F")
    elif m + f >= 80:
        result.append("A")
    elif m + f >= 65:
        result.append("B")
    elif m + f >= 50:
        if r >= 50:
            result.append("C")
        else:
            result.append("D")
    else:
        result.append("F")
for grade in result:
    print(grade)
```