a, b, c = map(int, input().split())
print(' '.join(sorted([str(x) for x in (c, min(a,b), max(a,b)]))