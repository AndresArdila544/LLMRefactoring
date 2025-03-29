x = list(input())
num = int(input())
for _ in range(num):
    v = input().split()
    order = v[0]
    a, b = map(int,v[1:]) if order!='print' else (map(int,v[1]),)
    if order == 'replace':
        del x[a:b+1]
        for n, v in enumerate(list(c)):
            x.insert(a + n, v)
    elif order == 'print':
        print(''.join(x[a:b+1]))
    elif order == 'reverse':
        c = x[a:b+1]
        del x[a:b+1]
        for n, v in enumerate(reversed(list(c))):
            x.insert(a + n, v)