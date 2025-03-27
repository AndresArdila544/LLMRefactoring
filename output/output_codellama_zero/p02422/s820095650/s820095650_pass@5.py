s=input()
q=int(input())
d_list=[]
for i in range(q):
    d = list(map(str, input().split()))
    if d[0]=='print':
        print(s[int(d[1]):int(d[2])+1])
    elif d[0]=='reverse':
        s=list(s)
        s[int(d[1]):int(d[2])+1]=reversed(s[int(d[1]):int(d[2])+1])
        for i in s:
            s+=i
    elif d[0]=='replace':
        s=list(s)
        s[int(d[1]):int(d[2])+1]=list(d[3])
        for i in s:
            s+=i