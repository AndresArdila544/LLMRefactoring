```python
import math

def manhattan_distance(x, y):
    return sum(abs(int(i) - int(j)) for i, j in zip(x, y))

def euclidean_distance(x, y):
    return math.sqrt(sum((int(i) - int(j))**2 for i, j in zip(x, y)))

def min_coord_distance(x, y):
    p = 3
    return sum(abs(int(i) - int(j))**p for i, j in zip(x, y)) ** (1/p)

def maximum_coordinate_difference(x, y):
    max_diff = float('-inf')
    for i, j in zip(x, y):
        max_diff = max(max_diff, abs(int(i) - int(j)))
    return max_diff

n = int(input())
x, y = input().split(), input().split()
print(manhattan_distance(x, y))
print(euclidean_distance(x, y))
print(min_coord_distance(x, y))
print(maximum_coordinate_difference(x, y))
```