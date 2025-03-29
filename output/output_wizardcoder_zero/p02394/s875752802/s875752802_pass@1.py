W, H, x, y, r = map(int, input().split())
print("Yes" if (x + r <= W) and (y + r <= H) and (0 <= x) and (0 <= y) else "No")