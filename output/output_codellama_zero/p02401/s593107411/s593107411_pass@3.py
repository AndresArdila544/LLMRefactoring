Here is a more concise and readable version of the program:

while True:
    x = input().split(" ")
    try:
        a, b = map(int, x[0], x[2])
        op = x[1]
        if op == "+":
            print(a+b)
        elif op == "-":
            print(a-b)
        elif op == "*":
            print(a*b)
        elif op == "/":
            print(a//b)
        elif op == "?":
            break
    except ValueError:
        continue