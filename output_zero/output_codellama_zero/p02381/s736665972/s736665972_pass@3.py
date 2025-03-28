import math

while True:
    n = int(input())
    if n == 0:
        break
    
    point = list(map(int, input().split()))
    
    m = sum(point) / len(point)
    
    temp = [(i - m)**2 for i in point]
    
    print('{0:.8f}'.format(math.sqrt(sum(temp)/n)))