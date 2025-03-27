def f(d):
    s = {'E':"310542",'S':"402351",'R':"031425"}
    a, b = input().split()
    for c in "SE":
        for i in range(4):
            d = [d[int(i)]for i in s[c]]
            for j in range(4):
                d = [d[int(i)]for i in s['R']]
                if d[0] == a and d[1] == b:
                    print(d[2])
                    return