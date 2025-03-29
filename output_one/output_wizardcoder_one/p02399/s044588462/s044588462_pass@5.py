a, b = map(int, input().split())
print(" ".join([str(i) for i in [a // b, a % b, a / b]])