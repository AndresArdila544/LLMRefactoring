a, b = map(int,input().split())
bs = [[list(map(int, input().split())) for i in range(a)] for j in range(b+1)]
for i in range(a):
    bs[i].append(sum(bs[i]))

for i in range(b+1):
    aa.append(sum([a[i] for a in bs]))

for i in bs:
    print(" ".join(map(str,i)))