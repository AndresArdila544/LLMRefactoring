Here is a refactored version of your code:

n = int(input())
a = [[0 for _ in range(10)] for __ in range(4)]
for i in range(n):
    b, f, r, v = map(int, input().split())
    a[b-1][f-1][r-1] += v
for j in range(4):
    for k in range(3):
        print(' '.join(str(x) for x in a[j][k]))
        if j != 3:
            print('####################')