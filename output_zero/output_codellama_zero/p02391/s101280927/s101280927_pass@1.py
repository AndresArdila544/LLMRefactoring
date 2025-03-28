# Refactoring the original program to reduce lines and complexity while preserving its functionality
a, b = map(int, input().split())
print(f"{a} {('<' if a < b else ('==' if a == b else '>'))} {b}")