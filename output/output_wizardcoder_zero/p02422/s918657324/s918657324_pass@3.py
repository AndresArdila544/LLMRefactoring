x = list(input())
num = int(input())
for i in range(num):
    v = input().split()
    order, a, b = v[0], map(int, v[1:3])
    if order == 'replace':
        c = input()
        x[a:b+1] = list(c)
    elif order == 'print':
        print(''.join(x[a:b+1])
    elif order == 'reverse':
        x[a:b+1] = list(reversed(x[a:b+1]))