def get_rectangle(height, width):
    return '#' * width

while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    print(get_rectangle(h, w))
    print('')