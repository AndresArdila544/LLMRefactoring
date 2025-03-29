def area_and_perimeter(s):
    a, b = map(int, s.split())
    m = a * b
    n = 2*a + 2*b
    return f"{m} {n}"