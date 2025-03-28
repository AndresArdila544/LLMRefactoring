Here is the refactored version of your program:
n, m = map(int, input().split())
a = [[int(x) for x in input().split()] for i in range(n)]
b = [int(x) for x in input().split()]
for k in range(n):
    print(sum(x*y for x, y in zip(a[k], b)))