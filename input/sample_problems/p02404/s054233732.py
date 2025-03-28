judge = True

while judge:
    N = list(map(int,input().split()))
    if N[0] + N[1] == 0:
        judge = False #finish
    else:
        for i in range(0, N[0]):# H
            print("#",end="")
            if i == 0 or i == (N[0] - 1):
                for j in range(1, N[1]-1):
                    print("#",end="")
                print("#")
            else:
                for j in range(1, N[1]-1):
                    print(".",end="")
                print("#")

    print("\n",end="")

