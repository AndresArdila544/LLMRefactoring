```python
while True:
    ins = input().split()
    h, w = map(int, ins)
    if h == 0 and w == 0:
        break
    for _ in range(h):
        print("#" * w)
```