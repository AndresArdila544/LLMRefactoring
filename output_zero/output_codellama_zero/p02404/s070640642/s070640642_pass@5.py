while True:
    h, w = map(int, raw_input().split())
    if not all((h,w)): break
    print("#" * w)
    for i in range(h - 3):
        print ("#" + "." * (w - 2) + "#")
    print ("#" + "." *(w-2)+"#")