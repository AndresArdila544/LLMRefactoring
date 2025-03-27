import math as mp
ans = []
while True:
    n = int(input())
    if n==0:
        break
    s = list(map(int,input().split()))
    m = sum(s)/len(s)
    ans.append( mp.sqrt(sum([(ele-m)**2 for ele in s])/len(s)) )
for ele in ans:
    print(ele)
