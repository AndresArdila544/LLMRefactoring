n, m = map(int, input().split())

a = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    a[i]= list(map(int, input().split()))

b = list()
for j in range(m):
    b.append(int(input()))

for k in range(n):
    print(int(sum(list(map(lambda x,y: x*y, a[k], b)))))
