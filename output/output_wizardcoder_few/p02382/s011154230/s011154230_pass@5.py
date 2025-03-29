```python
import math

def dist(A_lst, B_lst):
    s = 0
    for a, b in zip(A_lst, B_lst):
        s += abs(a - b) ** 1
    return math.pow(s, 1/1)
    
def pythagorean_dist(A_lst, B_lst):
    s = 0
    for a, b in zip(A_lst, B_lst):
        s += abs(a - b) ** 2
    return math.sqrt(s)
    
def manhattan_dist(A_lst, B_lst):
    s = 0
    for a, b in zip(A_lst, B_lst):
        s += abs(a - b)
    return s
    
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split())
print("{:.6f}".format(dist(A, B)))
print("{:.6f}".format(pythagorean_dist(A, B)))
print("{:.6f}".format(manhattan_dist(A, B)))
chebyshev = max(abs(a - b) for a, b in zip(A, B))
print("{:.6f}".format(chebyshev)
```

# Refactored version:
import math

def dist(*args):
    s = 0
    for a, b in zip(*args):
        s += abs(a - b) ** (1/1)
    return math.pow(s, 1/1)
    
def pythagorean_dist(*args):
    s = 0
    for a, b in zip(*args):
        s += abs(a - b) ** 2
    return math.sqrt(s)
    
def manhattan_dist(*args):
    s = 0
    for a, b in zip(*args):
        s += abs(a - b)
    return s
    
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split())
print("{:.6f}".format(dist(A, B)))
print("{:.6f}".format(pythagorean_dist(A, B))
print("{:.6f}".format(manhattan_dist(A, B)
chebyshev = max(abs(a - b) for a, b in zip(A, B))
print("{:.6f}".format(chebyshev)
```