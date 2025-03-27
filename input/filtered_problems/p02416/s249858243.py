while True:
    moji = str(input())
    if moji[0]=='0':
        break
    print(sum(int(num) for num in moji))
