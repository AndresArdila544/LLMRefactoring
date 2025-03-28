while True:
    a, b = map(int, input().split())
    if a and b:
        for i in range(a):
            print("#" * b)