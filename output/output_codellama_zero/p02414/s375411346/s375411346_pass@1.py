N,M,L = (int(i) for i in input().split())
A = [[int(i) for i in input().split()] for i in range(N)]
B = [[int(i)for i in input().split()] for i in range(M)]
C = [[ans] for ans in (sum(a*b for a,b in zip(A[i],B[i])) for i in range(N))]

print(*C, sep=" ")