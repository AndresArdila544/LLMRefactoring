def calculate(operator, a, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a // b
    else:
        break
while True:
    x = input().split()
    try:
        if len(x) != 3 or not all(isinstance(int(i) for i in x):
            raise ValueError("Invalid Input")
        a, op, b = int(x[0]), x[1], int(x[2])
    except (IndexError, ValueError):
        print("Invalid input")
        continue
    result = calculate(op, a, b)
    if op == "?":
        break
    print(result)