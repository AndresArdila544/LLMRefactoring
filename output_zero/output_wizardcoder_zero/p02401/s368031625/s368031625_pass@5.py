while True:
    a, op, b = map(int, input().split())   # 3変数ともに整数として読み込む
    
    if op=="?":
        break
    else:
        print({"+":a+b,"-":a-b,"*":a*b,"/":a//b}[op]