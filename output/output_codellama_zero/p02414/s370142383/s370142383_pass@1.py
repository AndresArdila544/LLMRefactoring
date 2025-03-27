n, m, l = map(int, input().split())

A = [[int(s) for s in input().split()] for i in range(n)]
B = [[int(s) for s in input().split()] for i in range(m)]

for x in range(n):
    o = [str(sum(a*b for a, b in zip(A[x], B[z]))) for z in range(l)]
    print(" ".join(o))