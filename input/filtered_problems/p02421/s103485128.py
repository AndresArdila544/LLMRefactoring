T=0
H=0
n=int(input())
for i in range(n):
    s=input()
    s=s.rstrip().split()
    if s[0]==s[1]:
        T+=1
        H+=1
    else:
        t=[s[0],"t"]
        h=[s[1],"h"]
        S=[t,h]
        S.sort()
        if S[1][1]=="t":
            T+=3
        elif S[1][1]=="h":
            H+=3
print(T,H)
