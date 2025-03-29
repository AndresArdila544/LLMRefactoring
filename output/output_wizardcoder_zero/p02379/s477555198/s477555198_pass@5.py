```python
import math 

def distance(u, v): 
    return math.sqrt((u.x - v.x) ** 2 + (u.y - v.y) ** 2)

a = [float(e) for e in input().split()]
print(distance(Point(*a[:2], Point(*a[2:]))
``` 

In this code, the distance function takes two points as inputs and calculates their Euclidean distance using the formula: `sqrt((x1 - x2)**2 + (y1 - y2)**2)`. The `*` operator in Python is used to unpack the list into positional arguments for the `Point` class, which are then passed as separate parameters.

We can shorten the code by using a lambda function to square each value and sum them up. This reduces the number of lines: 
```python
import math 
print(math.sqrt((lambda x,y:(x**2)+(y**2))(*a[:2])(*a[2:])))
```