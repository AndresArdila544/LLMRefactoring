x = list(input())
num = int(input())

for _ in range(num):
    v = input().split()
    order = v[0]
    if order == 'replace':
        a, b, c =v[1:]
        a, b = int(a), int(b)
        del x[a:b+1]
        for n, v in enumerate(list(c)):
            x.insert(a + n, v)
    elif order == 'print':
        a, b = map(int, v[1:])
        print(''.join(x[a:b+1]))
    elif order == 'reverse':
        a, b = map(int, v[1:])
        c = x[a:b+1]
        del x[a:b+1]
        for n, v in enumerate(reversed(list(c))):
            x.insert(a + n, v)