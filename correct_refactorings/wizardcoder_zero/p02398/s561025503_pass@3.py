a, b, c = list(map(int, input().split()))
print(len([i for i in range(a, b + 1) if not c % i]))