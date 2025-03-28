H, W = map(int, input().split())
for i in range(1, H+1):  # range start from 1 to H inclusive.
    print(''.join(['.' if j % 2 else '#' for j in range(W)])
H, W = map(int, input().split())
print('\n')
for i in range(1, H+1):  # range start from 1 to H inclusive.
    print(''.join(['.' if (j % 2 + i - 1) % 2 else '#' for j in range(W)]
H, W = map(int, input().split())