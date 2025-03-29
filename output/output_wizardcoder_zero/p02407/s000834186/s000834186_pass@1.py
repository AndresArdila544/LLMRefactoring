a = list(map(int, input().strip().split()))[::-1]
print(*a[1:], sep='')