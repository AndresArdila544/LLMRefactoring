while True:
    s = input()
    if s == '0':
        break
    else:
        print(sum(map(int,s)))