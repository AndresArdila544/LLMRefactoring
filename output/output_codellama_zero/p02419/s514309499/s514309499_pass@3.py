W = input()
    t = []
    count = 0
    c = 0
    
    while True:
        T = input()
        if T == "END_OF_TEXT":
            break
        else:
            t.append(T)
            c += 1
    
    for i in range(c):
        l = t[i].split()
        m = len(l)
        for j in range(m):
            if l[j].lower() == W:
                count += 1