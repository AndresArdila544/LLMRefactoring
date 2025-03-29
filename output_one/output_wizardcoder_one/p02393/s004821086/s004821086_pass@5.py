a,b,c=map(int,input().split())
d = min(a,b)
e = max(a,b)
f = c
if d > f :
    f = e
    e = d
print(f,e,d)