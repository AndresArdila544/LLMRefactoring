import math

def triangle_properties(a, b, C):
    S = (a * b * math.sin(math.radians(C))) / 2
    c = math.sqrt((a ** 2) + (b ** 2) - 2 * a * b * math.cos(math.radians(C)))
    L = a + b + c
    h = b * math.sin(math.radians(C))
    return S, L, h
    
a, b, C = map(int, input().split())
S, L, h = triangle_properties(a, b, C)
print(format(S, '.8f'))
print(format(L, '.8f'))
print(format(h, '.8f'))