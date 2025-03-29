while True:
    a = list(map(int, input().split()))
    if not a[0] and not a[1]: break
    min_a, max_a = (a[0], a[1]) if a[0] < a[1] else (a[1], a[0])