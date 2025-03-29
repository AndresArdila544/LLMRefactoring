N = int(input())
B = [[[0] * 10 for _ in range(3)] for _ in range(4)]

for i, b in enumerate(B):
    if i != 0:
        print('#' * 20)
    for f in b:
        print(' ', end='')
        print(*f)