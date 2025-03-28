from typing import List

def compute_area(x: int, y: int):
    return x * y


def compute_perimeter(x: int, y: int):
    return 2 * (x + y)


if __name__ == "__main__":
    x, y = map(int, input().split())
    area = compute_area(x, y)
    perimeter = compute_perimeter(x, y)
    print(f"{area} {perimeter}")