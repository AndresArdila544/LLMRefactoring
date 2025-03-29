Here is a refactored version of the code:

while True:
    H, W = map(int, input().split())
    if not (H and W):
        break
    print('#' * W for h in range(H))
    print()