def inRect(W, H, x, y, r):
    return all(0 <= coords <= max_dim for coords in (x-r, x+r, y-r, y+r) if isinstance(coords, int)) and 0 < r <= min(W, H)
print('Yes' if inRect(*map(int, input().split())) else 'No')