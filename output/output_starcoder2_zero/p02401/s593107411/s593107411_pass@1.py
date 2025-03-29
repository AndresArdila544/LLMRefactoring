Here is the original program that works as intended:

while True:
    x = input().split(" ")
    a = int(x[0])
    b = int(x[2])
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


Please give me the refactored version of this program, with fewer lines and improved readability: