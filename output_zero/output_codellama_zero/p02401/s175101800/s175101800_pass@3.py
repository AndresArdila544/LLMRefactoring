a, op, b = input().split()

if op == '?':
    break
elif op == '+':
    print(int(a) + int(b))
elif op == '-':
    print(int(a) - int(b))
elif op == '*':
    print(int(a) * int(b))
elif op == '/':
    print(int(a) / int(b))