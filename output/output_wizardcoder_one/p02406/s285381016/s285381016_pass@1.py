```python
n=int(input())
a = []
for i in range(1, n+1):
    if (i % 3 == 0) or (i % 10 == 3):
        a.append(i)
print(' ', end='')
print(*a)
``` 
```python
n=int(input())
[print(i, end=' ') if i%3==0 or i%10==3 else '' for i in range(1, n+1)]
```