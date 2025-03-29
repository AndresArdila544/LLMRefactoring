def inRect(*coords):
    W, H, x, y, r = coords
    return all(0 <= coord - r <= coord + r for coord in (x, y)) and 0 <= r <= max(W, H)

print('Yes' if inRect(*map(int, input().split()) else 'No')