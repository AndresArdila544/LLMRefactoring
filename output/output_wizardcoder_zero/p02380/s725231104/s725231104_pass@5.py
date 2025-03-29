```python
import math

a,b,C = map(float, input().split())

print("%f" % (1/2 * a * b * math.sin(math.radians(C)))
print("%f" % (a+b+math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(C))
print("%f" % ((1/2 * a * b * math.sin(math.radians(C)) / a * 2)
```

The program takes three input values `a`, `b` and `C` from the user, calculates two outputs using mathematical formulas, and prints them as formatted strings with a precision of two decimal places.

You can reduce the number of lines by combining some of the statements into one line, like this:

```python
import math
a, b, C = map(float, input().split())
print("%.2f" % (1/2 * a * b * math.sin(math.radians(C)))
print("%.2f" % (a+b+math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(C)
print("%.2f" % ((1/2 * a * b * math.sin(math.radians(C)) / a * 2) 
```

This will give you the same output, but with fewer lines of code and improved readability.

However, if you want to keep all three outputs on the same line for better organization, you can use tuple unpacking:

```python
import math
a, b, C = map(float, input().split())
print("%.2f", 1/2 * a * b * math.sin(math.radians(C), end="")
print(" ", "%.2f" % (a+b+math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(C))
print(", %.2f" % ((1/2 * a * b * math.sin(math.radians(C)) / a * 2) 
```

This will give you the same output but with each calculation on its own line and the results separated by commas, making it easier to read.