

a, b, c = map(int, input().split())

count = 0

for i in range(1, min(a, b) + 1):

    if c % i == 0 and c >= 1:

        count += 1

print(count)

