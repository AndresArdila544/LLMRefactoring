while True:
    x = input().split(" ")
    a, op, b = map(int, x)
    if op == "+": print(a+b)
    elif op == "-": print(a-b)
    elif op == "*": print(a*b)
    elif op == "/": print(a//b)
    elif op == "?": break