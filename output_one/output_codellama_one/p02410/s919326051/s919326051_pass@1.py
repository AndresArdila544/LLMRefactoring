n, m = map(int, input().split())
A = list()
for i in range(n):
    A.append([int(x) for x in input().split()])
B = [int(i) for i in input().split()]
res = [[sum(x * y for x, y in zip(a, b)) for a in A] for b in B]
for r in res:
    print(*r, sep=' ')