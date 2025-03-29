```python
h, w = map(int, input().split())
while h != 0 and w != 0:
    print(" "".join([("#" * (w + 2)]*2) + "\n"
              + ("#."*(w-2) + "#\n")*(h-3)
              + "#" * (w+1))
```