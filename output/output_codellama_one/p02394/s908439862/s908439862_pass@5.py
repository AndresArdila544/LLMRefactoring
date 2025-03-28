W, H, x, y, r = map(float, input().split())

if not (x > W - r and x < r and y < r and y > H - r):
    print("Yes")
else:
    print("No")