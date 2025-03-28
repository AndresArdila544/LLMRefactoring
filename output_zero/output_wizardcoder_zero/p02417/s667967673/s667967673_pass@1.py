list = []
try:
    while True:
        list.append(input())
except EOFError:
    pass
w = ''.join([x.lower() for x in list])
print('\n'.join(['{}: {}'.format(c, w.count(c)) for c in 'abcdefghijklmnopqrstuvwxyz'])