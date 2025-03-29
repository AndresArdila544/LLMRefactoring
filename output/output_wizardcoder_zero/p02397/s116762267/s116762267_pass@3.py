```python
while True:
    n = list(map(int,input().split()))
    if sum(n) == 0: break
    print(" ".join(sorted(str(x) for x in n))
```