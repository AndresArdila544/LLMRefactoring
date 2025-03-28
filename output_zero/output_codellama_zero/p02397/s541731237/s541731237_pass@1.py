a=[]
while True:
    n=input()
    if n=='0 0':break
    x,y=map(int,n.split())
    print(' '.join([str(max(x,y)), str(min(x,y))]))