import sys
H, W = map(int, input().split())
table = [[0]*(W+1) for i in range(H+1)]
for row, a in enumerate([list(map(int,input().split())) for _ in range(H)]):
    table[row][:W] = a
for col in range(1, W+1):
    table[:H] = [row[col] + row[0] for row in table]
table[H][:] = [row[0] + row[col] for col in range(W) for row in table]
for row in table:
    print(" ".join([str(i) for i in row]))