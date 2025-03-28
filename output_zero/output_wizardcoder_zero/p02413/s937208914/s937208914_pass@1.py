```python
a = []
gyou = [0] * c
retu = []
s = 0
for i in range(r):
    a_i = list(map(int, input().split()))
    retu.append(sum(a_i))
    gyou = [x + y for x, y in zip(gyou, a_i)]
    s += sum(a_i)
for i in range(c):
    print(" ".join(map(str, a[i]), retu[i])
    if i == c - 1:
        print(" ".join(map(str, gyou), s)
```