import itertools
c = [''.join([str(x) + str(y) for x, y in itertools.product(['S', 'H', 'C', 'D'], range(1, 14))])
for _ in range(int(input())):
    c.remove(input())
if c: print('\n'.join(c))