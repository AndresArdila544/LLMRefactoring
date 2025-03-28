import sys
r, c = map(int, input().split())
ans = []
for i in range(r):
    tmp = list(map(int, input().split()))
    tmp.append(sum(tmp))
    ans.append(tmp)
    str_tmp = [str(s) for s in tmp]
    str_tmp = " ".join(str_tmp)
    print(str_tmp)

tmp = []
for i in range(c+1):
    total = 0
    for j in ans:
        total += j[i]
    tmp.append(total)
    
str_tmp = [str(s) for s in tmp]
str_tmp = " ".join(str_tmp)
print(str_tmp)