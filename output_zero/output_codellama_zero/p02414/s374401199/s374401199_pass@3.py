n, m, l = map(int, input().split())
A = []
B = []
C = []
for i in range(n):
    A.append([int(x) for x in input().split()])

for i in range(m):
    B.append([int(x) for x in input().split()])
#積を求める

C = [A[i] + B[i] for i in range(n)]
#形式に合わせて出力する
for line in C:
    print(*line)