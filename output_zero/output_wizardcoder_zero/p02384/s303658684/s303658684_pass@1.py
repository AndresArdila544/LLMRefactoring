def roll_dice(d):
    a1,a2,a3,a4,a5=map(int,input().split())
    q=int(input())
    
    for _ in range(q):
        c=["E","W","S","N"]
        roll_idx = random.randint(0,2)
        while (d[0]!=a1 or d[1]!=a2) and d[roll_idx] != a3:
            d=sorted([a4,a2,a6,a5,a3][:4-roll_idx]+[a1,a5,a4,a6])
        print(d[-1])
        
roll_dice(list(map(int,input().split()+input().split()))