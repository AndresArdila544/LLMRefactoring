while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        b_even = "." * (b // 2) + "#" * ((b + 1) % 2)
        b_odd = "#" * (b // 2) + "." * ((b + 1) % 2)
        for i in range(a):
            if i % 2 == 0:
                print(b_even)
            else:
                print(b_odd)
        print("")