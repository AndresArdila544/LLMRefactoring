a, b = map(int, input().split())
bs = [[int(num) for num in input().split()] for i in range(a)]
for i in range(a):
    bs[i].append(sum(bs[i]))
aa = [sum([a[i] for a in bs]) for i in range(b+1)]
bs.append(aa)
for i in bs:
    print(" ".join(map(str, i)))