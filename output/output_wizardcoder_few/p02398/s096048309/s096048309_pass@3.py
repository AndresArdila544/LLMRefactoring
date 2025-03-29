a, b, c = map(int, input().split())
print((c//2) + (b*(c-1)) - ((a-1)*(c//2) if a > 1 else 0)