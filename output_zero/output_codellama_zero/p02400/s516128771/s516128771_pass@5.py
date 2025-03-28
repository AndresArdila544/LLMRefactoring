import math

def circle_area(radius):
    area = math.pi * radius ** 2
    circumference = math.pi * (2*radius)
    
    return area, circumference

r = float(input())
rs, r_r = circle_area(r)
print(rs, r_r)