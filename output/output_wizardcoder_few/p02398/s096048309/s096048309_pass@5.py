a, b, c = map(int, input().split())
sum(i % j == 0 for i in range(a, b + 1) if (c % j) == 0)
print()