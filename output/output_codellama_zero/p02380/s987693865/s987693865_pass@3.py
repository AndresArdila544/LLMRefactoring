Here is a refactored version of the Python program with fewer lines and improved readability:
import math
input_values = list(map(int, input().split()))
a, b, angle = input_values
rad = (angle / 180) * math.pi
c = ((a ** 2 + b ** 2 - 2 * a * b * math.cos(rad)) ** 0.5)
s = (a+b+c)/2
S = (s*(s-a)*(s-b)*(s-c))**0.5
print(format(S,".5f"))
print(format(a+b+c,".5f"))
print(format((2*S)/a,".5f"))