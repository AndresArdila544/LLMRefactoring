n = int(input())
while n != 0:
    point = list(map(int, input().split()))
    m = sum(point)/len(point)
    temp = [(i - m)**2 for i in point]
    print('{0:.8f}'.format(math.sqrt(sum(temp)/n)))
    n = int(input())