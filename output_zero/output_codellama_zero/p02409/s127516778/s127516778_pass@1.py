N = int(input())
B = [[[0] * 10 for _ in range(3)] for _ in range(4)]
for _ in range(N):
    b, f, r, v = map(int, input().split())
    B[b - 1][f - 1][r - 1] += v

for b in B:
    if b:
        print('#' * 20)
    for f in b:
        print(' ', end='')
        print(*f)