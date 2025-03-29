num, pat, sum = [], [], []
i = int(0)
N = int(0)
while True:
    num = list(map(int, input().split(' ')))
    if all(x == 0 for x in num):
        break
    else:
        pat.append(num[0])
        sum.append(num[1])
        N += 1
i = 0
while i < N:
    s = 0
    for k in range(1, pat[i] + 1):
        for l in range(k + 1, pat[i] + 1):
            for m in range(l + 1, pat[i] + 1):
                if sum[i] == k + l + m:
                    s += 1
    print(s)
    i += 1