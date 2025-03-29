x = list(input())
n = int(input())
for _ in range(n):
    order, *args = input().split()
    if order == 'replace':
        a, b, *c = map(int, args)
        x[a:b+1] = c
    elif order == 'print':
        a, b = map(int, args)
        print(''.join(x[a:b+1]))
    elif order == 'reverse':
        a, b = map(int, args)
        x[a:b+1] = reversed(x[a:b+1])