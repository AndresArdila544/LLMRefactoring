Here's the refactored code:
```
n=int(input())
for i in range(1,n+1):
    if i%3==0:
        print(" "+str(i),end="")
    else:
        while int(i/10)%10!=3 and i>0:
            i=int(i/10)
print("")
```