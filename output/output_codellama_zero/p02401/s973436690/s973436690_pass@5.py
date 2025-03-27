while True:
    a, op, b = input().split() 
    if op=="?":
        break
    print(eval(f"{a}{op}{b}"))