```python
while True:
    cnt = 0
    n, x = map(int, input().split())
    if n == 0 or x == 0: break
    for i in range(1,n-1):
        for j in range(i+1,n):
            cnt+=sum([1 for k in range(j+1,n) if (i + j + k) == x])
    print(cnt)
```