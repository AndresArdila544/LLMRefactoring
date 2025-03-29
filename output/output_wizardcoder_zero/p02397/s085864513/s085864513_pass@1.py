while True:
    a = list(map(int, input().split()))
    if a == [0, 0]: break
    for x in sorted(a): print(x)