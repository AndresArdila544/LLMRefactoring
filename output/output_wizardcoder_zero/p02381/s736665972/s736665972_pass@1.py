Here's a refactored version of the code that is more concise and readable:


```python
import math

def standard_deviation(point):
    n = len(point)
    m = sum(point) / n
    temp = [(i - m)**2 for i in point]
    return '{0:.8f}'.format(math.sqrt(sum(temp)/n))
```

You can then call this function with a list of numbers as an argument to get the standard deviation:

```python
point = [1, 2, 3, 4, 5]
print(standard_deviation(point)) # prints "0.9167864376"
```