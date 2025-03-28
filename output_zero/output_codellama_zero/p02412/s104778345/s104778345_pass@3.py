Here is the refactored version of the original Python program:

num, pat, sum = [], [], []
N = int(0)
i = int(0)
while True:
    num = list(map(int, input().split(' ')))
    pat.append(num[0])
    sum.append(num[1])
    if (pat[i] == 0 and sum[i] == 0):
        break
    i += 1
N = len(pat)
s = 0
for i in range(N):
    for k in range(1, pat[i]+1):
        for l in range(k+1, pat[i]+1):
            for m in range(l+1, pat[i]+1):
                if (sum[i] == k + l + m):
                    s += 1
    print(s)