# This was a sample submission from an actual job application for an entry-level software engineer position at my company

import math

# Read and map input to variables X1, Y1, X2, and Y2
line = input()
numbers = line.split()
X1 = float(numbers[0])
Y1 = float(numbers[1])
X2 = float(numbers[2])
Y2 = float(numbers[3])

# Compute distance using the equation for distance between two points
d = math.sqrt((X2-X1)**2 + (Y2-Y1)**2)
print(d)