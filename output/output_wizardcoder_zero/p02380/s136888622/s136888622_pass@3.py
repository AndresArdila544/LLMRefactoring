```python
import math
a, b, C = map(int, input().split())
S = 0.5 * a * b * math.sin(C/180*math.pi)
L = a + b + math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(C/180*math.pi))
h = b * math.sin(C/180*math.pi)
print(S, L, h, sep="\n")
```

Explanation: 
The original program takes three inputs from the user and calculates the surface area (S), length of side (L) and height (h) of a triangle using Heron's formula. The `math` module is imported to use pi and trigonometric functions.

The refactored code splits the functionality into separate lines for each variable, which improves readability and makes it easier to maintain in case more variables need to be added or if more calculations are needed in future versions of the program. The `sep` argument is used to print all three values on different lines using a single print statement.