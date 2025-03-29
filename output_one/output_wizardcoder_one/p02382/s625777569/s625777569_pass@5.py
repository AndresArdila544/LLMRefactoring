```python
import math

def manh(x, y):
    return sum(abs(int(i) - int(j)) for i, j in zip(x, y))

def uqurid(x, y):
    return math.sqrt(sum(abs(int(i) - int(j) ** 2 for i, j in zip(x, y)))

def minco(x, y):
    p = 3
    return max(abs(int(i) - int(j) for i, j in zip(x, y)) ** p

def ebis(x, y):
    d = 0
    for i, j in zip(x, y):
        d = max(d, abs(int(i) - int(j)
    return d

n = int(input())
x = input().split()
y = input().split()
print(manh(x, y))
print(uqurid(x, y))
print(minco(x, y))
print(ebis(x, y))
```