r, c = map(int, input().split())
a = []
for i in range(r):
    a.append([sum(list(map(int, input().split())))])
print(*a[::-1], sep=' ')
print(sum(a[c]))