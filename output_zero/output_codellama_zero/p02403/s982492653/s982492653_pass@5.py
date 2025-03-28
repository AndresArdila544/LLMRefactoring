while True:
    HM = input()
    if not HM:
        break
    for H, M in (map(int, i.split()) for i in HM.split(" ")):
        print("#" * M)
        if H == H - 1:
            print()