W, H, x, y, r = map(int, input().split(' '))
if x > 0 and y > 0 and x + r >= 0 and y + r > 0 and (W - r - x) >= 0 and (H - r - y) >= 0:
    print('Yes')
else:
    print('No')

