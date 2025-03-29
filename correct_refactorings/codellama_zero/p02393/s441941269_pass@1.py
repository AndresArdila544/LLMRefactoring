a, b, c = map(int, input().split())
s, g = sorted([a, b])
print(' '.join(map(str, sorted([c, s, g]))))