W, H, x, y, r = map(float, input().split())
if not (x > W - r) and not (x < r) and not (y < r) and not (y > H - r):
    print("Yes")
else:
    print("No")