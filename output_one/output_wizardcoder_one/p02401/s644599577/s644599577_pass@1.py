a, op, b = map(int, input().split())

while True:
    if op == "?":
        break
    elif op == "+":
        a += b
    elif op == "-":
        a -= b
    elif op == "*":
        a *= b
    elif op == "/":
        a //= b
    print(a)
    op, b = input().split()
    a, op, b = int(a), int(b), 0