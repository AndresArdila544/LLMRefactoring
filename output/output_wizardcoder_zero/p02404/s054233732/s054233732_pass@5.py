```python
for i in range(N[0] - 2):
    print("#" * (i == 0 or i == N[0] - 1) + "." * (N[1] - 2) + "#" * (i != 0 and i != N[0] - 2)
```