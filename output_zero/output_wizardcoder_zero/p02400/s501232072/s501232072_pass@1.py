```python
import math
def circle_area(r):
    return round(math.pi * r ** 2, 6)

def circle_circumference(r):
    return round(2 * math.pi * r, 6)

if __name__ == '__main__':
    print(circle_area(float(input()), circle_circumference(float(input())))
```
```python
import math
def circle_functions(r):
    return round(math.pi * r ** 2, 6), round(math.pi * 2 * r, 6)
if __name__ == '__main__':
    print(*circle_functions(float(input()))
``` 
The code has been refactored by creating a function `circle_functions` that takes in the radius as an argument and returns both the area and circumference of the circle. This way, we can call this function once with both results returned at the same time instead of calling it twice separately.

Using tuple unpacking to print the values with a single line is also more concise and efficient than calling the function twice.