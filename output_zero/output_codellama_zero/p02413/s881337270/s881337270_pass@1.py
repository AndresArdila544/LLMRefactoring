r, c = map(int, input().split())
ans = []
for i in range(r):
    tmp = list(map(int, input().split()))
    tmp.append(sum(tmp))
    ans.append(tmp)
    
print(' '.join(['{}'.format(item) for item in ans]))