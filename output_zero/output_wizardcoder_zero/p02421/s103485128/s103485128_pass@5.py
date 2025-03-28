T=0; H=0
n=int(input())
for i in range(n):
    s=input().rstrip().split()
    if s[0]==s[1]: T+=1
    else:
        t=[s[0],"t"]
        h=[s[1],"h"]
        S=[t,h]
        S.sort(); T+=(S[1][1]=="t")*3; H+=(S[1][1]=="h")*3
print(T,H)