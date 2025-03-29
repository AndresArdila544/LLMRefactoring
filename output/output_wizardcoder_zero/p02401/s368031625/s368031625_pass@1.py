a = input().split()[0]   # 入力の最初の要素を取り出す
b = int(input().split()[1])    # 2番目の要素をintに変換して取り出す
c = input()

while c != '?':   
    a, op, b = map(int, a.split())     # 3変数ともに文字列からintへ変換
    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        print(a // b)