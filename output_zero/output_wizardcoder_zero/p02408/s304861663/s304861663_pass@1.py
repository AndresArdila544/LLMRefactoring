c = [f'{x}{y}' for x in 'SHCD' for y in range(1, 14)]
for _ in map(int, input().split()):
    c.remove(''.join(map(str, _))
if c: print('\n'.join(c))