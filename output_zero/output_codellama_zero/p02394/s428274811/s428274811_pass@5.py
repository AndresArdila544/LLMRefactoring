W, H, x, y, r = map(int, input().split())
print("Yes" if (x+r <= W and x-r >= 0) and (y+r <= H and y-r >= 0) else "No")