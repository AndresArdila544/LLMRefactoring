a,b,c=map(int,input().split())
s=0

for i in range(a,b+1):
    if(i==0):
        i=i+1
    else:    
        if c%i == 0:
            
            s=s+1
            i=i+1

print(s)
    
