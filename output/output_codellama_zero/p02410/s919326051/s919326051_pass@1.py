n, m = map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
for i in range(len(A)):
    value = 0
    for j in range(len(B)):
        value += A[i][j] * B[j]
        print(value)