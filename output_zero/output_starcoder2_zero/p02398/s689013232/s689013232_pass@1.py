Here is what I came up with:

a, b, c = map(int, input().split())
count = 0
for num in range(a,b+1):
    if c % num == 0:
        count += 1
print(count)


Can someone give me an example of a good refactor with a single line?