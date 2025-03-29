import math
while True:
    n = int(input())
    if n == 0:
        break
    point_list = list(map(int, input().split()))
    mean = sum(point_list) / len(point_list)
    temp = [(x - mean)**2 for x in point_list]
    print('{0:.8f}'.format(math.sqrt(sum(temp)/n)))