import sys
H, W = map(int, input().split())
table = [[0]* (W+1) for i in range(H+1)]

for row in range(H):
    a = list(map(int,input().split()))
    for col in range(W):
        table[row][col] = a[col]

for row in range(H):
    for col in range(0, W):
        table[row][W] += table[row][col]

for col in range(0,W+1):
    for row in range(0, H):
        table[H][col] += table[row][col]
        
for row in range(0,H+1):
    print("%d"%(table[row][0]),end="")
    for col in range(1,W+1):
        print(" %d"%(table[row][col]),end = "")
    print()