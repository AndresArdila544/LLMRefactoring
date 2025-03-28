def in_rect(W, H, x, y, r):
    return all((0 <= x-r <= W, 0 <= y-r <= H, x+r <= W, y+r <= H)
print('Yes' if in_rect(*map(int, input().split())) else 'No')