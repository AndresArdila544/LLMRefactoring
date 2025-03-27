a, b, c = list(map(int, input().split()))

count = 0
for num in range(a, b+1):
    if c % num == 0:
        count += 1
print(count)
