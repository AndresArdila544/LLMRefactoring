n=int(input())
var=input()
var=var.split()
i=n-1
while(True):
    if(i==0):
        print(var[0])
        break
    else:
        print(var[i]+" ",end='')
        i-=1
