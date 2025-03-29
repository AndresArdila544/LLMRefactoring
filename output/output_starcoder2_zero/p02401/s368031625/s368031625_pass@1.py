Here is my solution:
while True:
    a, op, b = input().split()    # 3変数ともに文字列として読み込む
    a =int(a)                    # a を整数に変換
    b = int(b)                    # b を整数に変クト
    
    if (op=="?"):
        break;

    print(eval(f"{a}{op}{b}"))