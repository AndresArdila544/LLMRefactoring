a, b, c = map(int, input().split())
s = sum(i for i in range(a, b + 1) if i % c == 0 and i != 0)
print(s)