def f(d):
    s = {'E':"310542",'S':"402351",'R':"031425"}
    for c in "SE":
        for i in range(4):
            d[i] = [int(d[i]) for i in s[c]]
        for j in range(4):
            d[j] = int(s['R'])
            if d == ['310542', '402351']:
                print('0')
                return

d = [input().split() for _ in range(int(input()))]
for i in d: f(i)