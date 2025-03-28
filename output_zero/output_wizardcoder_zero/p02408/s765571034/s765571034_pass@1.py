n=int(input())
for m in ['S','H','D']:
    for n in range(1,13+1):
        if (m,str(n)) not in [(x[0], str(x[1])) for x in [(c, int(p)) for c, p in [input().split()] for i in range(n)]]:
            print(m, n)