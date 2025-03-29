def inRect(W, H, x, y, r): return (0 <= x-r <= x+r <= W) and (0 <= y-r <= y+r <= H)
print('Yes' if inRect(*map(int, input().split())) else 'No')