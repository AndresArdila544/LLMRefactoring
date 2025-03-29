```
while True:
    H, W = map(int, input().split())
    if not H and not W:
        break
    for i in range(H):
        print(''.join(['#' if (i + j) % 2 else '.' for j in range(W)]))
    print()
```