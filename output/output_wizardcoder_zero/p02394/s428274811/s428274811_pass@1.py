W, H, x, y, r = map(int, input().split())
print("Yes" if all([x+r <= W, x-r >= 0, y+r <= H, y-r >= 0]) else "No")