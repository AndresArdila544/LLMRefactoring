if __name__ == "__main__":
    while True:
        H, W = map(int, raw_input().split())
        if H == 0 and W == 0:
            break
        for i in range(H):
            line = ""
            for j in range(W):
                if (i + j) % 2 == 0:
                    line += "#"
                else:
                    line += "."
            print line