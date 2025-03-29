```python
import math

r = float(input())
rs = r * r * math.pi
r_r = 2 * r * math.pi
print(rs)
``` 
The program calculates the area and circumference of a circle given its radius.
First, it takes the input value for `r` from the user and stores it as a float in variable `r`. Then, it calculates the area of the circle using formula `pi*r^2` (where r is the radius) and stores the result in `rs`. It also calculates the circumference of the circle using formula `2*pi*r` and stores the result in a new variable `r_r`. Finally, it prints the value of `rs`, which represents the area, and `r_r`, which represents the circumference.