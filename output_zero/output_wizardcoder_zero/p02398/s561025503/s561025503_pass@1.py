x = input().split()
a, b, c = map(int, x)
print(len([i for i in range(a, b+1) if not c%i])