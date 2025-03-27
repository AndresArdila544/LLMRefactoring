a, b = list(map(int, input().split()))
c = 0
for num in range(a, b+1):
    if c % num == 0:
        c += 1
print(c)