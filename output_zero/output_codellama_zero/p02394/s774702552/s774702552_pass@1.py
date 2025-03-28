W, H, x, y, r = map(int, input().split())
W -= r
H -= r
if r <= x <= W and r <= y <= H:
    print("Yes")