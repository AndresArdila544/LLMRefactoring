a, b, c = list(map(int, input().split()))
print((c // (a + (b - a) % (b - a))) - 1)