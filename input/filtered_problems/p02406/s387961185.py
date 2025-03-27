a = int(input())
for x in range(1,a+1):    
    if x % 3 == 0: 
        print(" {}".format(x),end="")
    else:
        if "3" in str(x):
            print(" {}".format(x),end="")
        else:
            continue
