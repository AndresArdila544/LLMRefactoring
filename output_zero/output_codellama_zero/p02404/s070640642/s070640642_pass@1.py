while True:
    h, w = map(int, raw_input().split())
    if h == w == 0: break
    print "#" * w
    for i in range(h - 3):
        print("#" + "." * (w - 2) + "#" + "\n")
    print "#" + "." * (w - 2) + "#"