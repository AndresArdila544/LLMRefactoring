```python
import math

def manhattan_distance(x, y):
    return sum(abs(int(i)-int(j)) for i, j in zip(x, y))

def euclidean_distance(x, y):
    return math.sqrt(sum(abs(int(i) - int(j))**2 for i, j in zip(x, y))

def manhattan_distance_modified(x, y):
    d = 0
    for i, j in zip(x, y):
        d += abs(int(i) - int(j)
    return d

def uniformity_coefficient(x, y):
    p = 3
    return max(abs(int(i) - int(j))**p for i, j in zip(x, y))**(1/p)

n = int(input())
x = input().split()
y = input().split()

print(manhattan_distance(x, y))
print(euclidean_distance(x, y))
print(manhattan_distance_modified(x, y))
print(uniformity_coefficient(x, y))
```