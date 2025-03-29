HM = input("Enter Hours and Minutes separated by space (0 0 to exit): ")
while HM != '0 0':
    H, M = map(int, HM.split())
    for _ in range(H):
        print("#" * M)
        if _ == H - 1: 
            print()