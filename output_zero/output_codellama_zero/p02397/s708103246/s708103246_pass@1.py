while True:
    a, b = map(int, input().split())
    if not (a == 0 and b == 0):
        print(*sorted([a, b], reverse=b >= a), sep="\n")