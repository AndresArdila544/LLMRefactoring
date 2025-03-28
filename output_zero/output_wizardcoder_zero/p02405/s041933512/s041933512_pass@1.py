H, W = map(int, input().split())
for i in range(H):
    print('#' * (W//2) + '.'*(W%2)) if (i+1) % 2 == 0 else print('.')*W
print()
while H != 0 or W != 0:
    H, W = map(int, input().split())