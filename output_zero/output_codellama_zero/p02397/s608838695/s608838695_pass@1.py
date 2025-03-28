while True:
    x, y = map(int, input().split())
    if not (x and y):
        break
    print(*sorted([x, y]))