```python
import math

def calculate_area(radius):
    return round(math.pi * radius**2, 6)

def calculate_circumference(radius):
    return round(math.pi * 2 * radius, 6)

if __name__ == '__main__':
    try:
        r = float(input())
        print("Area of the circle is", calculate_area(r))
        print("Circumference of the circle is", calculate_circumference(r))
    except ValueError:
        print("Invalid input. Please enter a valid radius value.")
```