```python
tate, yoko = map(int, input().split())
menseki = tate * yoko
syuu = 2 * (tate + yoko)
print(menseki, syuu)
```

```python
# Refactored version:
t, y = map(int, input().split())
m = t * y
s = 2 * (t + y)
print(m, s)