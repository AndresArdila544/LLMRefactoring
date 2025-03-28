```python
while True:
    n = int(input())
    if n==0: break
    l = list(map(float, input().split()))
    avg=sum(l)/len(l)
    sigma_squared=sum((x-avg)**2 for x in l)
    print ((sigma_squared/n)**0.5)
```