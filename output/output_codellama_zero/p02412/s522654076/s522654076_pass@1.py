import sys
a,b = map(int,sys.stdin.readline().split())
while a!=0 or b!=0:
    c = 0
    for i in range(1,a+1):
        for j in range(i+1,a+1):
            if (i+j)==b:
                c=c+1
    a,b = map(int,sys.stdin.readline().split())
print(c)