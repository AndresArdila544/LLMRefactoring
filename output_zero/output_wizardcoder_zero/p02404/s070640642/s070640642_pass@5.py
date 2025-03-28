```python
while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    print("".join([("#" * w + "\n"] * (h - 3) + ["#" + "." * (w-2) + "#\n"]) + ("#" * w)
```