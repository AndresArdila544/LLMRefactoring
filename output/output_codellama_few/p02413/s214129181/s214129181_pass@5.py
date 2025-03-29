n,m = map(int, input().split())
bs= [[sum([int(i) for i in input().split()])] +list(map(int,input().split())) for j in range(n)]
for j in range(n):
    bs[j].append(sum(bs[j]))
aa = []
for i in range(m+1):
    aa.append(sum([a[i] for a in bs]))
bs.append(aa)
for i in bs:
    print(" ".join(map(str, i)))