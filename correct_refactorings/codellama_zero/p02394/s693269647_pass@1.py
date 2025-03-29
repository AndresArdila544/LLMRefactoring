def in_rect(W, H, x, y, r):
    return (0 <= x-r <= x+r <= W) and (0 <= y-r <= y+r <= H)
print('Yes' if in_rect(*map(int, input().split())) else 'No')