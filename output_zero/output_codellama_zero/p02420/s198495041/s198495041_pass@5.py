while True:
    c = input()
    if c == "-": break
    m = int(input())
    for i in range(m):
        h = int(input())
        c += C[0:h]
        C = C[h:len(C)+1]
    print(C)