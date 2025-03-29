Here is the original Python program:

import sys

n, m, l = map(int, input().split())

mat_a  = []
mat_b  = []
for i in range(n):
    array  = list(map(int, input().split()))
    mat_a.append(array)

for i in range(m):
    array  = list(map(int, input().split()))
    mat_b.append(array)

ans = 0
for i in range(n):
    for k in range(l):
        for j in range(m):
            ans += mat_a[i][j] * mat_b[j][k]
        if k != 0: print(' ', end='')
        print('{}' .format(ans), end='')
        ans = 0
    print()