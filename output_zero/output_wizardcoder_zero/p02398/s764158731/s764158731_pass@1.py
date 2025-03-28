a, b, c = map(int, input().split())
print((c//2) - ((1 if a > 0 and b // a else 0) + (b//c)) * c)