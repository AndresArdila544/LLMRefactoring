a, b = map(int, input().split())
print(*map(str, (a // b, a % b, a / b))