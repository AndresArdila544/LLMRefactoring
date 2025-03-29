a, b, c = map(int, input().split())
count = sum((i % 10000 >= 1 and i % 1 <= 10000) for i in range(1, max(b+1)) if (c % i == 0))
print(count)