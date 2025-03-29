import math

tate, yoko = map(int, input().split())
print(tate * yoko, 2*tate + 2*yoko) 

This is a refactored version of the code that reduces its lines and improves readability. It calculates the area and perimeter of a rectangle by using the given input values for tate (width) and yoko (length). The area formula is tate * yoko, and the perimeter formula is 2*tate + 2*yoko. Both formulas have been combined into one print statement to reduce the code's complexity.

Refactored version: 
```python
import math
tate, yoko = map(int, input().split())
print(tate * yoko, 2*tate + 2*yoko)
```