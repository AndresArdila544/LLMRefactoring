a,b,c = map(int,input().split())
if a>b and b<c or c<a:
    print(a,b,c)
elif a>c and b>c:
    print(c,a,b)
else:
    print(b,c,a)