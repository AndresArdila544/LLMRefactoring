new_list = []
try:
    while True:
        new_list.append(input().lower())
except EOFError:
    pass

print('\n'.join([f'{c}: {w.count(c)}' for c in 'abcdefghijklmnopqrstuvwxyz'])