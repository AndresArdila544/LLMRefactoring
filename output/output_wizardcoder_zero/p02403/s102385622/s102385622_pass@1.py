```python
while True:
    ins = input().split()
    h, w = map(int, ins)
    if not all(ins):
        break
    for _ in range(h):
        print("#" * w)
```