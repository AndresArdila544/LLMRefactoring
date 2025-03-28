import math
a, b, c = map(int, input().split())

if c <= 90:
    if a >= b:
        A, B = a, b
    else:
        A, B = b, a
    
    print((B * math.sin(math.radians(c)) * A) / 2)
    h = B * math.sin(math.radians(c))
    X = (B**2 - h**2) ** 0.5
    C = ((A-X)**2 + h**2)**0.5
    print(C+a+b)
else:
    H = B * math.sin(math.radians(c))
    
    if a >= b:
        A, B = a - H, b
    else:
        A, B = b - H, a
    print((B**2 + H**2) ** 0.5)
    h = B * math.sin(math.radians(c))
    x = (b**2 - h**2) ** 0.5
    c = ((A)**2 + h**2) ** 0.5
    print(c+a+b)
    print(h)

This code is more concise, reduces the number of lines and improves readability by avoiding unnecessary variables and using a single if statement to determine which value is the larger or smaller for A and B. It also uses proper formatting for code blocks.