x = list(input())
num_lines = int(input())
for i in range(num_lines):
    order, *args = input().split()
    if order == 'replace':
        a, b, *c = map(int, args)
        x[a:b+1] = c
    elif order == 'print':
        a, b, *_ = map(int, args)
        print(''.join(x[a:b+1]))
    elif order == 'reverse':
        a, b, *_ = map(int, args)
        x[a:b+1] = reversed(x[a:b+1])