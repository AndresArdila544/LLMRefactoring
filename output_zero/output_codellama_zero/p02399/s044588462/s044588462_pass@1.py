def get_values():
    a, b = map(int, input().split())
    return (a // b, a % b, a / b)

print(*get_values(), sep=' ')