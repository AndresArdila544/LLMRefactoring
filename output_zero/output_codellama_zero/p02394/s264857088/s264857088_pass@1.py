import sys

W, H, x, y, r = map(int, input().split())
x1, x2 = max(0, x-r), min(W, x+r)
y1, y2 = max(0, y-r), min(H, y+r)
if not all((x1 <= W and x2 >= 0), (y1 <= H and y2 >= 0)):
    print("No")
else:
    print("Yes")