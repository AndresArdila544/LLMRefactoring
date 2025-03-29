```python
import math
x1, y1, x2, y2 = map(float, input().split())
print(round(math.hypot(x2-x1, y2-y1), 8))
```

Explanation: 
The program calculates the distance between two points using the Pythagorean theorem and the `math` module's `hypot()` function. It reads in four values as input, namely x1, y1, x2, and y2, converts them to floats using `map()`, subtracts the second set of coordinates from the first, and then takes the square root of the sum of their squares using `** 0.5`. Finally, it rounds the result to 8 decimal places and prints it out.

Refactoring this code by removing unnecessary variables and directly calculating the distance with `hypot()` function reduces the number of lines of code from 4 to 2 while also improving readability. 

Note: The `round()` function is used to round off the output to 8 decimal places. If you want more or less precision, simply change the second argument accordingly.