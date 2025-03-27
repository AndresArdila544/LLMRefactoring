Below is a Python program that works as intended, but I need you to refactor the code to reduce its lines and complexity, while preserving its functionality. Make the code cleaner, more concise, and improve its readability.

Here is the original Python program:

import math

a,b,c=map(int,input().split())
if c<=90:
    print(b*math.sin(math.radians(c))*a/2)
    h=b*math.sin(math.radians(c))
    A=max(a,b)
    B=min(a,b)
    H=B*math.sin(math.radians(c))
    X=(B*B-H*H)**0.5
    C=((A-X)**2+H*H)**0.5
    print(C+a+b)
    print(h)
else:
    print(b*math.sin(math.radians(c))*a/2)
    A=a-b*math.cos(math.radians(c))
    h=b*math.sin(math.radians(c))
    x=(b*b-h*h)**0.5
    c=((A)**2+h*h)**0.5
    print(c+a+b)
    print(h)