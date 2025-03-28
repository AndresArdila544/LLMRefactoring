```python
while True:
    n = list(map(int, input().split()))
    if n[0] == 0 and n[1] == 0:
        break
    print(" ".join(str(sorted(n)))
```