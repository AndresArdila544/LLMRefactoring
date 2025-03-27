import math
while True:
  n,x = map(int,input().split())
  if n == 0 and x == 0: break
  count = sum([1 for u in range(math.ceil(x/3),n+1) if u-v > v >= w for v in range((x-u)//2 + 1, x-u) for w in range(x-u-v+1) if u > v > w])
  print(count)