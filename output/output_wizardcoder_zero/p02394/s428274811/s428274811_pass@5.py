def check_coordinates(W, H, x, y, r):
    return "Yes" if x+r <= W and x-r >= 0 and y+r <= H and y-r >= 0 else "No"

print(check_coordinates(*map(int, input().split()))