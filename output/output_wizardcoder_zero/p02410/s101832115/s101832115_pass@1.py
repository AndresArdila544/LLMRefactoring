n, m = [int(x) for x in input().split()]
a = [[0]*m for _ in range(n)]
b = [0]*m
c = [0]*n
for i in range(n):
    a[i] = [int(x) for x in input().split()]
    b[i] = int(input())
for i in range(n):
    c[:] = [sum(a_row * b_val for a_row, b_val in zip(a[i], b)) for i in range(m)] 
print(*c)