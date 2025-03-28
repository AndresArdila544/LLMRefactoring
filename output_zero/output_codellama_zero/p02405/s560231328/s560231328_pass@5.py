if __name__ == "__main__":
    while True:
        H, W = map(int, raw_input().split())
        if H == 0 and W == 0:
            break
        so = "#" * W + "\n"
        for i in range(1, H, 2):
            print ".#." * W + "\n"
        if H & 1:
            print so