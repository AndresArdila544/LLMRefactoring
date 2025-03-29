```python
import math
a, b, C = map(int, input().split())
s = (a * b) * math.sin(math.radians(C)) / 2
print((a+b) + ((a**2 + b**2 - 2*a*b*math.cos(math.radians(C)))**0.5))/2 # Reduced complexity by using parenthesis and removing redundant variables.
print((s * 2)/a)
```

The code calculates the area of a right triangle and the height, without the use of a new variable 'c'. The code also reduces the number of lines and improves readability.