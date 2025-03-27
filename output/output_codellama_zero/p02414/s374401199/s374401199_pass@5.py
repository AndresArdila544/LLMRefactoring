n, m, l = map(int, input().split())
A= []
B= []
for i in range(n):
    A.append([int(x) for x in input().split()])
for i in range(m):
    B.append([int(x) for x in input().split()])
#積を求める
C = [list(sum(a*b for a, b in zip(A[i], B[j]))) for i in range(n) for j in range(l)]
#形式に合わせて出力する
for line in C:
    print(*line)