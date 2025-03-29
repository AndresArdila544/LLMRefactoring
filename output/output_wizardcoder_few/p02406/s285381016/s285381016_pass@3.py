```python
n = int(input())
a=[]
i = 1
c = 0
while i <= n:
    if c == 0 and (i % 3 == 0 or str(i) in '3'): a.append(i)
    elif i%10 == 3: a.append(i)
    else: i *= 10
    i += 1
print(*a, sep=' ', end='\n')
```