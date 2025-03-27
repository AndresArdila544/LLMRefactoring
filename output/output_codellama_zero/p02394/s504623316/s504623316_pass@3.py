W, H, x, y, r = map(int, input().split(' '))
print('Yes') if (0 < x <= W-r and 0 < y <= H-r) else print('No')