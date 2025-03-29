```python
a = []
n = int(input())
for i in range(1, n + 1):
    if not (i % 3) and (str(i).count('3') == 0):
        a.append(i)
print(' ', end='')
print(*a)
```