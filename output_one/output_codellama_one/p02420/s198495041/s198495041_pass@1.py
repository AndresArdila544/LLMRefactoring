while True :
    C = input()
    
    if C == "-" :
        break
    else :
        m = int(input())
        
        for i in range(m) :
            h = int(input())
            c = input().rstrip("\n")[0:h]
            C = C[:h]+c+C[h:]