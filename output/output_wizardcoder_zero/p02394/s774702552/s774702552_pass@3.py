W, H, x, y, r = map(int, input().split())
print("Yes" if (x <= W and x + r <= W) and (y <= H and y + r <= H) else "No")