N = int(input())
B = [[0]*10 for _ in range(4)]
for i in range(N):
    b, f, v = map(int, input().split())
    B[b-1][f-1] += v
for r in [B[i:i+3] for i in range(0, 12, 3)]:
    print('#' * 20)
    print(''.join(['   '*9]) if i%3==0 else ' '.join(map(str,r)) for i,_ in enumerate(range(4)))