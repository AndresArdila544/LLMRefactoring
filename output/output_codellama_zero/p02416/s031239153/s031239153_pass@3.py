while True:
    x = input()
    if x == '0':
        break
    else:
        print(sum(list(map(int, x))))