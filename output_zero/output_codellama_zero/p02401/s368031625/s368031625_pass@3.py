while True:
    a, op, b = input().split()
    print(eval(f"{a} {op} {b}"))
    if op == "?":
        break