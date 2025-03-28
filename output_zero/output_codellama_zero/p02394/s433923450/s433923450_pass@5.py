def check_coordinates(W, H, x, y, r):
    if x >= r and x <= W - r and r <= y and y <= H - r:
        return "Yes"
    else:
        return "No"