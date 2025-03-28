```python
while True:
    try:
        a, op, b = map(int, input().split())  # 3変数ともに整数として読み込む
        
        if op == "?":
            break
        elif op == "+":
            print(a + b)
        elif op == "-":
            print(a - b)
        elif op == "*":
            print(a * b)
        elif op == "/":
            print(a // b)  # // で除算を行うことで小数点以下の端半分が切り捨てられる
    except ValueError:
        pass # a, bの変換に失敗した場合は何も表示せず、処理をスキップする
```