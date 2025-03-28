Original Program:
import sys
lines = sys.stdin.readlines()
while True:
    n=0
    x=0
    cnt=0

    try:
        line = lines.pop(0)
        line = line.strip().split(" ")
        n = int(line[0])
        x = int(line[1])

        if n==x==0:
            break

    except IndexError as e:
        break

    for i in range(1,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if x == i+j+k:
                    cnt+=1
    print(cnt)