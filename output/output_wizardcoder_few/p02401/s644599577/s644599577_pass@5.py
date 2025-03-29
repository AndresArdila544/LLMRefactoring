def operator_calculator():
    for _ in range(int(input())):
        a, op, b = input().split()
        a, b = int(a), int(b)
        if op == "+":
            ans = a + b
        elif op == "-":
            ans = a - b
        elif op == "*":
            ans = a * b
        elif op == "/":
            ans = a // b
        print("{}".format(ans))
        
operator_calculator()