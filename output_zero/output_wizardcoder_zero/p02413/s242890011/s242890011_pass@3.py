import sys
H, W = map(int, input().split())
table = [[0] * (W+1) for i in range(H+1)]
for row in range(H):
    a = list(map(int, input().split()))
    for col in range(W):
        table[row][col] = a[col]

# transpose the table and add rows to columns
for i in range(1, H+1):
    for j in range(1, W+1):
        table[i].append(table[j][i-1])

# print table with a space separator between numbers
for row in range(H+1):
    for col in range(W+1):
        print("{}".format(table[row][col], end=" ")
    print()