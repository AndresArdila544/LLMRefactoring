a, b = map(int, input().split())
print(' '.join([str(x) for x in [a // b, a % b, a / b]])