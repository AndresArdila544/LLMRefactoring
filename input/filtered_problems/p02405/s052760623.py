H,W=map(int,input().split())
while (W>0 and H>0):
    for i in range(H):
        for j in range(W):
            if (i%2==0):
                if (j%2==0):
                    print("#",end="")
                elif ((j+1)%2==0):
                    print(".",end="")
            elif ((i+1)%2==0):
                if ((j+1)%2==0):
                    print("#",end="")
                elif (j%2==0):
                    print(".",end="")
        print()
    print()
    H,W=map(int,input().split())
