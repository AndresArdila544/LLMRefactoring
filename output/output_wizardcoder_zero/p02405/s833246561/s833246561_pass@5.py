for _ in range(int(input())):
    H,W=map(int, input().split())
    a="."*(W+1)[:-1] if W%2==0 else "#"*((W+1)//2)+"."*(W//2)
    b="#"*(H//2)+".("#"*(H//2 if H%2!=0 else (H//2))
    print(a.center(W,"#").join([b,b[::-1] for _ in range(H)])