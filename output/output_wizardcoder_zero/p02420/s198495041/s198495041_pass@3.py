while True:
    C = input()
    
    if C == "-":
        break
    else:
        m = int(input())
        h = [int(input()) for i in range(m)]
        C, c = list(C), []
        for i in range(len(h)):
            c.append(C[0:h[i]] + input() + C[h[i]:])
            C = "".join(c)
        print(C)