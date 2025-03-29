Here is a Python program that works as intended, but I need you to refactor the code to reduce its lines and complexity, while preserving its functionality. Make the code cleaner, more concise, and improve its readability.
import math
x1, y1, x2, y2 = map(float, raw_input().split())
distance = (x2 - x1)**2 + (y2 - y1)**2
print math.sqrt(distance)