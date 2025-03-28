a, op, b = map(int, input().split())

while True:
    if op == "?":
        break
    elif op == "+":
        print(a+b)
    elif op == "-":
        print(a-b)
    elif op == "*":
        print(a*b)
    elif op == "/":
        print(a//b)
    a, op, b = map(int, input().split())