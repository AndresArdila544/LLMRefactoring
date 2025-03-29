def inRect(W, H, x, y, r):
    return ((0 <= x-r) and (x+r <= W)) and ((0 <= y-r) and (y+r <= H)) 

print('Yes' if inRect(*map(int, input().split())) else 'No')