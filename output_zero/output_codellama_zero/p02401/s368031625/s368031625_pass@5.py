while True:
    a, op, b = input().split()   # 3変数ともに文字列として読み込む
    a =int(a)                   # a を整数に変換
    b = int(b)                   # b を整数に変換
    



    if op=="?": 
        break
    else: #opが"?"以外の時
        print(eval(f"{a}{op}{b}"))