from sys import stdin
input = stdin.readline
i = 0
while True:
    num = int(input())
    if not num:break
    i += 1
    print('Case %d: %d'%(i, num))