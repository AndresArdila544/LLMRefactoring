a = sorted(list(map(int, input().split())))
print(a[0], end = '')
for x in range(1, len(a)):
    print(" %d" % a[x], end = '')
