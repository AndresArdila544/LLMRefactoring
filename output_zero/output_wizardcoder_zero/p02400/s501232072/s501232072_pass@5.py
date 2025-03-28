```python
import math

def compute_circumference_area(r):
    return round(math.pi * r**2, 6), round(2*math.pi*r, 6)

if __name__ == '__main__':
    r = float(input())
    circumference, area = compute_circumference_area(r)
    print(f"Circumference: {circumference}, Area: {area}")
```