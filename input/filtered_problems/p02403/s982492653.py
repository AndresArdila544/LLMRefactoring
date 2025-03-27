while True:
    HM = input()
    HM_list = HM.split(" ")
    H = int(HM_list[0])
    M = int(HM_list[1])
    if H == 0 and M == 0:
        break
    for x in range(H):
        print("#" * M)
        if x == H - 1:
            print()
