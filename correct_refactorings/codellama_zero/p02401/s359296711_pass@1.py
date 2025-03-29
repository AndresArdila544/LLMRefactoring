# encoding:utf-8

while True:
    a,op,b = map(str, input().split())
    c = int(a)
    d = int(b)
    result = None 
    
    if op == '+': result = c + d
    elif op == '-': result = c - d
    elif op == '*': result = c * d
    elif op == '/': result = int(c / d)
    elif op == '?': break
    else: break
    
    print("{0}".format(result))