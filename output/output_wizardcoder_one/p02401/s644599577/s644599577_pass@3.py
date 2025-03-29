a, op, b = map(int, input().split())
while True:
    try:
        a, op, b = map(int, input().split())
        if op == "?":
            break
        elif op == "+":
            print("{}".format(a + b))
        elif op == "-":
            print("{}".format(a - b)
        elif op == "*":
            print("{}".format(a * b)
        else:
            print("Invalid operator")
    except ValueError:
        break