while True:
    a, b = map(int, input().split())
    if a == 0: break
    for i in range(a):
        print("#"*b)
    print()
