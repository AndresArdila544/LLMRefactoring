import math as mp
for n in iter(int,0):
    s = list(map(int,input().split()))
    m = sum(s)/len(s)
    ans.append( mp.sqrt(sum([(ele-m)**2 for ele in s])/len(s)) )
for ele in ans:
    print(ele)