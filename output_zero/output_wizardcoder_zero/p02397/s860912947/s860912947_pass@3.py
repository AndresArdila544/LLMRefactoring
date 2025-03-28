```python
a = []
b = []
while True:
    x,y = map(int,input().split())
    if x == 0 and y == 0:
        break
    a.append(x)
    b.append(y)
for i in range(len(a)):
    print(f'{b[i]}, {a[i]}' if a[i] >= b[i] else f'{a[i]}, {b[i]}')
```