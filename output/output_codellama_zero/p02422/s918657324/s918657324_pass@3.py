Here is a refactored version of the program that has been simplified:

x = list(input())
num = int(input())

for _ in range(num):
    v = input().split()
    order = v[0]
    if order == 'replace':
        a, b, c =v[1:]
        x[a:b+1] = list(c)
    elif order == 'print':
        a, b = map(int, v[1:])
        print(''.join(x[a:b+1]))
    elif order == 'reverse':
        a, b = map(int, v[1:])
        x[a:b+1] = reversed(list(x[a:b+1]))