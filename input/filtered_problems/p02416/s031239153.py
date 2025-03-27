while True:
    x = input()
    if x == '0':
        break
    else:
        x_list = list(map(int, x))
        goukei = sum(x_list)
        print(goukei)
