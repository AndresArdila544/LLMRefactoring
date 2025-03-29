n = int(input())
a = [[0 for _ in range(10)] for _ in range(4) for _ in range(3)]  # Initialize a with zeros
for i in range(n):
    b, f, r, v = map(int, input().split())
    a[b-1][f-1] += v
for j in range(4):
    print(' '.join([str(a[j][k]) for k in range(10)] + ['\n'])  # Iterate through each row and print its values separated by spaces
    if j != 3:
        print('#' * 25  # Print a line of 25 '#' characters between rows, but not at the last one.