while True:
    a = list(map(int, input().split()))
    if a == [0, 0]: break
    print(" ".join(str(x) for x in a))