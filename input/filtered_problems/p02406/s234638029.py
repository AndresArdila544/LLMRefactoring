# coding: utf-8
num = int(input())
i = 0
print(" ",end="")
while (i != num):
    i+=1
    if i % 3 == 0:
        print(i, end="")
        if i != num:
            print(" ", end="")
    elif "3" in str(i):
            print(i, end="")
            if i != num:
                print(" ",end="")
print("")