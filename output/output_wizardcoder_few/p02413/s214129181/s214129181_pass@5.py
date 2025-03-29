a, b = map(int, input().split())
bs = [list(map(int, input().split()) for i in range(a))
for i in range(a):
    bs[i].append(sum(bs[i]))
aa = []
for i in range(b+1):
    aa.append(sum([a[i] for a in bs])
print(*(map(str, bs + [aa]), sep=' ')