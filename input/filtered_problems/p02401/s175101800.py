
while True:
    a, op, b= input().split()
    
    if op == '?':
       break
    if op == '+':
        print(int(a) +int(b))
    elif op == '-':
        print(int(a) - int(b))
    elif op == '*':
        print(int(a) * int(b))
    elif op == '/':
        print(int(int(a) /int(b)))
    
