```
N = list(map(int,input().split()))
judge = N[0]+N[1]!=0
while judge:
    print("################" * N[0])
    if judge:
        for i in range(0, N[0]):# H
            print("#",end="")
            if i == 0 or i == (N[0] - 1):
                for j in range(1, N[1]-1):
                    print("#",end="")
                print("#")
            else:
                for j in range(1, N[1]-1):
                    print(".",end="")
                print("#")
        judge = False  # finish
```