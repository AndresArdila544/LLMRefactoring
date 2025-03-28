Refactored solution:

while True :
    C = input()
    
    if C == "-" :
        break 
    else :
        m = int(input())
        
        for i in range(m) :
            h = int(input())
            c  = C[0 : h]
            C  += c
            C   = C[h :]
            
        print(C)