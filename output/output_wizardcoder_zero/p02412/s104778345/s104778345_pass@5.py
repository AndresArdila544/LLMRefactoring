num, pat, sum = [], [], []
i = int(0)
N = int(input())
while 1:
    num_str = input().split()
    if len(num_str) == 2 and num_str[0].isdigit() and num_str[1].isdigit():
        num.append(int(num_str[0]))
        sum.append(int(num_str[1]))
        if pat[-1] == 0 and sum[-1] == 0:
            break
    else:
        print("Invalid input.")
        continue
    i += 1
N = len(pat)
for k in range(1, N):
    s = 0
    for l in range(k + 1, pat[i] + 1):
        for m in range(l + 1, pat[i] + 1):
            if sum[i] == k + l + m:
                s += 1
    print(s)