```python
import math

def main():
    r = float(input())
    print(round(math.pi * pow(r, 2), 6)) # rounding to 6 decimal places is optional here
    print(round(math.pi * 2 * r, 6))
```
This code calculates the area and perimeter of a circle given its radius, rounded to 6 decimal places.
```python
import math

def main():
    r = float(input())
    print("{:.6f}".format(math.pi * pow(r, 2))) # rounding to 6 decimal places is optional here as well
    print("{:.6f}".format(math.pi * 2 * r))
```
We can use string formatting for the output in order to avoid multiple calls to `round()` function. We can also remove the redundant function definition and call it directly from `main()`.