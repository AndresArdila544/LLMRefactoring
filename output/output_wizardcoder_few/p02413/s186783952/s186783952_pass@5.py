```python
n,m=map(int,input().split())
for i in range(n):
    a = []
    for j in range(m+1):
        a += list(map(int, input().split()))
        if j == m:
            print(sum(a[:-1]), end=' ')
```