while True:
    a, op, b = [int(i) if i.isnumeric() else i for i in input().split()]  # take user inputs as integers or strings
    if op == '?': break  # exit loop when "?" is entered
    elif op == '+': print(a + int(b))  # perform addition and output result
    elif op == '-': print(a - int(b))  # perform subtraction and output result
    elif op == '*': print(a * int(b))  # perform multiplication and output result
    elif op == '/': print(a // int(b))  # perform floor division and output result
    else:  # if input is not a valid operator, repeat the loop
        print("Invalid operation.")