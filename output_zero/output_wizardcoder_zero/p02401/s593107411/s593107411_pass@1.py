while True:
    try:
        a, op, b = map(int, input().split())
        if op == '+':
            print(a + b)
        elif op == '-':
            print(a - b)
        elif op == '*':
            print(a * b)
        elif op == '/':
            print(a // b)
        elif op == '?':
            break
    except ValueError:
        pass