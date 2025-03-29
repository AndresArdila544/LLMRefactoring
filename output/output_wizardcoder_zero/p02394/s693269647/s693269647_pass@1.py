def in_rect(width, height, x, y, radius):
    return (0 <= x - radius <= width) and (0 <= y - radius <= height)

print('Yes' if all(in_rect(*map(int, input().split())) else 'No')