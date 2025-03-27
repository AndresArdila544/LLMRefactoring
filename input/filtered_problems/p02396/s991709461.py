from sys import stdin
input = stdin.readline

i = 0
while True:
    num = int(input())
    if num == 0:
        break
    i += 1
    print('Case %d: %d'%(i, num))
