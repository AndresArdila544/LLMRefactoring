a, b, c = map(int, input().split())
print(sum(i for i in range(a, b+1) if c % i == 0))