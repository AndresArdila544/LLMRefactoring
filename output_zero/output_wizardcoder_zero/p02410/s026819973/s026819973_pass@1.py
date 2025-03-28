n, m = map(int, input().split())
a = [[0]*m for i in range(n)]
b = list(map(int, input().split()))*n
for k in range(n):
    print(sum(x * y for x,y in zip(a[k], b)))