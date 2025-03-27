def inRect(W, H, x, y, r):
    if not (0 <= x-r <= x+r <= W):
        return False

    if not (0 <= y-r <= y+r <= H):
        return False

    return True

print('Yes' if inRect(*map(int, input().split())) else 'No')
