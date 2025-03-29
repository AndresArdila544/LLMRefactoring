N = int(input())
B = [[0]*10 for _ in range(4)]
for _ in range(N):
    b, f, v = map(int, input().split())
    B[b-1][f-1] += v