def area(a, b):
    return a * b


def perimeter(a, b):
    return (a + b) * 2


if __name__ == "__main__":
    s = input()
    a, b = map(int, s.split())
    print(area(a, b), perimeter(a, b))