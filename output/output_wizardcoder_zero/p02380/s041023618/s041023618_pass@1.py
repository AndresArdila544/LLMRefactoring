import math
a, b, C = map(int, input().split())
s = (a*b) * math.sin(math.radians(C)) / 2
print((a**2 + b**2 - 2*a*b*math.cos(math.radians(C))**0.5) ** 0.5) # Calculate c and then use it to calculate s, h as follows:
h = (s*(2/a) # Convert s to h using a. 
print(round((a+b+(c)), 1) # Rounding off the result to one decimal place.