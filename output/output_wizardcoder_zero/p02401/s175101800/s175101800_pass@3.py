a, op, b = input().split() # combine these two lines into one line
while True:
    if op == '?':
        break
    else:
        print(eval(f'{int(a)} {op} {b}'))