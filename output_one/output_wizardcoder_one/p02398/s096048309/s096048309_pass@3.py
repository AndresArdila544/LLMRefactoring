a, b = map(int, input().split())
divisible_count = sum([1 for i in range(a, b+1) if c % i == 0])
print(divisible_count)