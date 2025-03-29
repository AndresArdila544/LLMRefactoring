num, pat, sum = [], [], []
i = int(0)
N = int(0)
while 1:
    num = list(map(int, input().split(' ')))
    if not (pat[i] == 0 and sum[i] == 0):
        break
    pat.append(num[0])
    sum.append(num[1])
    i += 1
    N += 1
s = 0
for k in range(N):
    for l in range(k + 1, pat[i]):
        for m in range(l + 1, pat[i]):
            if sum[i] == k + l + m:
                s += 1
    print(s)
    i += 1