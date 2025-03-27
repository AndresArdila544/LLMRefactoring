while True:
    a,b=map(int, input().split())
    if a==0 and b==0:
        break
    else:
        b_str="#"*b
        for i in range(a):
            print((i%2)*b_str)