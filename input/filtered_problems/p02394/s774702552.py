W, H, x, y, r = map(int, input().split())

W -= r
H -= r

if r <= x and x <= W and r <= y and y <= H:
    print("Yes")
else:
    print("No")
