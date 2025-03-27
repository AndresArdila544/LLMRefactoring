def tri_area(a, b, c):
    a = float(a)
    b = float(b)
    c = math.radians(c)
    S = (a * b * math.sin(c)) / 2
    L = a + b + (math.sqrt(a*a + b*b - 2*a*b*math.cos(c)))
    H = (2*S)/a
    return [S, L, H]