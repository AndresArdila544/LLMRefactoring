```python
while True:
    try:
        n = int(input())
        if not n: break
        cnt = 0
        for i in range(1, n):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if sum((i, j, k) == x:
                        cnt += 1
        print(cnt)
    except ValueError:
        break
```