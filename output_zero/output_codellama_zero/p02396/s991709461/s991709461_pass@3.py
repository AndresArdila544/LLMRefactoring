from sys import stdin
input = stdin.readline
for i in range(1,int(num)+1):
        num = int(input())
        if num == 0:
                break
        print('Case %d: %d'%(i, num))