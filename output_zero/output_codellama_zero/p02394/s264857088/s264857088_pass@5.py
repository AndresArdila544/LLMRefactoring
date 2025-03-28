W, H, x, y, r = map(int, input().split())
x1, x2 = max(0, x-r), min(W, x+r)
y1, y2 = max(0, y-r), min(H, y+r)
if not (x1 <= x2 and y1 <= y2):
    print("No")
else:
    print("Yes")