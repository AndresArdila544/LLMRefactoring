import math

def calculate_average(point):
    return sum(point)/len(point)

while True:
    temp = []
    n = int(input())
    if n == 0:
        break
    point = list(map(int, input().split()))
    m = calculate_average(point)
    for i in point:
        temp.append((i - m)**2)
    print('{0:.8f}'.format(math.sqrt(sum(temp)/n)))