Here is the refactored code:

a, b = map(int, input().split())
bs = [[int(i) for i in input().split()] for _ in range(a)]
for i in range(a):
    bs[i].append(sum(bs[i]))
aa = [sum([bs[i][j] for j in range(b+1)]) for i in range(a)]
bs.append(aa)

for i in bs:
    print(" ".join(map(str,i)))