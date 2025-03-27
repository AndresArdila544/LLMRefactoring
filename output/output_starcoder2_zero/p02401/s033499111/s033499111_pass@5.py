Here is my proposed solution:

while 1:
    a, op, b = map(str, raw_input().split())
    a = int(a)
    b = int(b)

    if op == "+":
        print(a+b)
    elif op == "-":
        print(a-b)
    elif op == "*":
        print(a*b)
    elif op == "/":
        print(a/b)
    elif op == "?":
        break

Note: I used Python 3 to write the above code. In Python 2, `print` is a function instead of a statement.