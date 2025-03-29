n, m = [int(x) for x in input().split()]
a = [[0]*m for _ in range(n)]
b = [0]*m
c = [0]*n
for s in range(n):
    a[s] = [int(x) for x in input().split()]
    b[s] = int(input())
    c[:] = (a_row * b_val for a_row, b_val in zip(a, b))
for t in range(n):
    print(sum(c))