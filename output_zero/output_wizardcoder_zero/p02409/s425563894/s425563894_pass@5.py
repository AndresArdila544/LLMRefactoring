n = int(input())
a = [[0 for _ in range(3)] for _ in range(4)]  # create a 2D list of size (4 x 3) with all elements initialized to 0
for _ in range(n):
    b, f, r, v = map(int, input().split())
    a[b - 1][f - 1] += v

# print the values in each row of the matrix
for c in range(4):
    for d in range(3):
        print('', end='')
        for e in range(3):
            print(a[c][d], end=' ')
    print()
    if c != 3:
        print('#' * 20) # print a separator line between each row, except the last one
        
# The original code is already concise and easy to read. There are no further suggestions on reducing its complexity or lines.