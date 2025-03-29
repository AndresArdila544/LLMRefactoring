while True:
    HM = input()
    if not HM: break
    for x in range(int(HM.split(" ")[0])):
        print("#" * int(HM.split(" ")[1]))
        if x == int(HM.split(" ")[0]) - 1: print()