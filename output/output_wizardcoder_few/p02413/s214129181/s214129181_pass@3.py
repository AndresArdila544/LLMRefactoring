```python
a, b = map(int,input().split())

for _ in range(b):
    bs = [list(map(int, input().split())) + [sum(bs)] for i in range(a) for bs in [[]]][:-1]
print(*(" ".join(str(sum(i)) for i in zip(*([input().split()]*(b+1)))), sep=' ')
```