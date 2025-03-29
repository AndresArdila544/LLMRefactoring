while True:
    m,f,r = list(map(int,input().split()))
    if (m==-1 and f==-1) or m+f<30:
        print("F")
    elif m+f>=50 and r<50:
        print("D")
    elif m+f>=65 and r<50:
        print("C")
    elif m+f>=80:
        print("B")
    else:
        print("A")