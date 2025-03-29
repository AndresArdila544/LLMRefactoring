```python
a = []
n = int(input())
i = 1
while i <= n:
    if not i % 3 and i != 0:
        a.append(i)
    elif i % 10 == 3:
        a.append(i)
    else:
        x = int(str(i)[:-1])
        if x == 0:
            continue
        i += 1
print(' ', end='')
print(*a)
```