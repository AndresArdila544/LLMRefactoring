def count_triplets(x):
    n = int(input())
    if not x: return 0
    
    cnt = 0
    for a in range(1, n):
        for b in range(a+1, n):
            ab = a + b
            if ab >= x: break
            
            for c in range(b+1, n):
                abc = ab + c
                
                if abc == x:
                    cnt += 1
                    
                elif abc > x:
                    break
                    
    return cnt

while True:
    try:
        print(count_triplets(int(input()))
    except EOFError:
        break