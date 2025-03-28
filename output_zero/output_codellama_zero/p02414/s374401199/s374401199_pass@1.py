n, m, l =map(int, input().split())
A = []
B = []
C = []
for i in range(n):
    A.append([int(j) for j in input().split()])

for i in range(m):
    B.append([int(j) for j in input().split()])

#積を求める
C = [[sum(a*b for a, b in zip(A[i], B[j])) for j in range(l)] for i in range(n)]

#形式に合わせて出力する
for line in C:
    print(*line)