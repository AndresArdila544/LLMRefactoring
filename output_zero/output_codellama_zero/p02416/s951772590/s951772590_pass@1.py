while True:
    s = input()
    if s == "0":
        break
    a = sum(int(x) for x in s)
    print(a)