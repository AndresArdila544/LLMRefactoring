while True:
    m, f, r = map(int, input().split())
    if m==-1 or f==-1 or r == -1:
        break
    x=max(0,m)+max(0,f)
    if m==-1 or f==-1:
        grade='F'
    elif 80<=x:
        grade='A'
    elif 65<=x and x<80:
        grade='B'
    elif 50<=x and x<65:
        grade='C'
    elif 30<=x and x<50:
        if 50<=r:
            grade='C'
        else:
            grade='D'
    else:
        grade='F'
    print(grade)