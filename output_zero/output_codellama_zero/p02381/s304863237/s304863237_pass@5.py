import math

while True:
    n = int(input())
    
    if n == 0:
        break
    
    data = list(map(int, input().split()))
    
    m = float(sum(data) / n)
    
    aa = sum(((i - m) ** 2) for i in data)/n
    
    a = math.sqrt(aa)
    print(a)