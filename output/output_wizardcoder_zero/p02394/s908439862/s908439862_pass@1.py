def check_circle(W, H, x, y, r):
    if (x > W - r) or (x < r) or (y < r) or (y > H - r):
        return "No"
    else:
        return "Yes"