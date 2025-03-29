def inRect(W, H, x, y, r):
    return (0 <= x-r <= W and 0 <= y-r <= H) and (-r <= x <= W + r and -r <= y <= H)

print('Yes' if inRect(*map(int, input().split()) else 'No')