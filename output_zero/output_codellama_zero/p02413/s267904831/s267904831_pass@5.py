r, c = map(int, input().split())
a = [0]*(c+1)
for _ in range(r):
    v = list(map(int, input().split()))
    a = [x+y for x, y in zip(a, v)]
print(*a)