def area(a, b):
    return a * b


def perimeter(a, b):
    return (a + b) * 2

s = input().split()
a, b = map(int, s)
print(area(a, b), perimeter(a, b))