n, m = map(int, input().split())
A = list()
b = list()
for i in range(n):
    A.append([int(x) for x in input().split()])
for i in range(m):
    b.append(int(input()))
for i in range(n):
    _=0
    for j in range(m):
        _ += A[i][j] * b[j]
    print(_)