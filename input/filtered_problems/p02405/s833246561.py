while True:
    H,W=input().split()
    H,W=[int(H),int(W)]
    if H==0 and W==0:
        break
    a=""
    b=""
    for i in range(0,W):
        if i%2==0:
            a=a+"#"
            b=b+"."
        else :
            a=a+"."
            b=b+"#"
    for i in range(0,H):
        if i%2==0:
            print(a)
        else :
            print(b)
    print()
        
