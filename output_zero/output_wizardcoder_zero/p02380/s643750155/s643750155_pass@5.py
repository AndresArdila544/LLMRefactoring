a, b, c = map(int, input().split())
radius = c * (math.pi / 180) # convert to radians for trigonometry functions
if c <= 90:
    semi_major_axis = a * math.sin(radius) * 2 # calculate semi-major axis for the first case
    if b >= a: # check which is longer side
        max_side, min_side, h = a, b, b * math.sin(radius)
    else:
        max_side, min_side, h = b, a, a * math.sin(radius)
    
    semi_minor_axis = min_side * math.sin(radius) # calculate semi-minor axis
    x = (min_side ** 2 - semi_minor_axis ** 2) ** 0.5 # calculate x value for the first case
    C = ((max_side - x) ** 2 + h ** 2) ** 0.5 # calculate C value for the first case
    print(C + a + b)
    print(h)
else:
    semi_major_axis = a * math.cos(radius) # calculate semi-major axis for the second case
    if a >= b: # check which is longer side
        max_side, min_side, h = a, b, b * math.sin(radius)
    else:
        max_side, min_side, h = b, a, a * math.sin(radius)
    
    x = (min_side ** 2 - h ** 2) ** 0.5 # calculate x value for the second case
    C = ((max_side - x) ** 2 + h ** 2) ** 0.5 # calculate C value for the second case
    print(C + a + b)
    print(h)