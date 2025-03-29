```python
a=[]
n=int(input())
while n > 0:
    if n % 3 == 0:
        a.append(n)
    elif n % 10 == 3:
        a.append(n)
    n //= 10
print(' ', end='')
print(*a) 
```