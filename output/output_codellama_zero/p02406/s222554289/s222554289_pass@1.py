```
n = int(input())
for i in range(1, n+1):
    if i%3==0:
        print(" " + str(i), end="")
    else:
        temp=i
        while temp>0:
            if temp%10==3:
                print(" " + str(i), end="")
                break
            temp = int(temp/10)
print("")
```