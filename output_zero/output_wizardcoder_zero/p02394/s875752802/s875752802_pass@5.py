W, H, x, y, r = map(int, input().split())
print("Yes" if (x + r <= W) and (y + r <= H) and (-r <= x <= W - r) and (-r <= y <= H - r) else "No")