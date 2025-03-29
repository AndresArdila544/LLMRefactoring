n=int(input())
for m in ['S','H','D']:
    for n in range(2,14):
        if (m,str(n)) not in [c[0]+str(c[1]) for c in [(i[0],i[1]) for i in [input().split() for _ in range(n)]]: print(m,n)