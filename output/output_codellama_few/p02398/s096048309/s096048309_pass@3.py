a, b, c = map(int, input().split())
d = sum(c % i == 0 for i in range(a, b + 1))
print(d)