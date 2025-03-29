import math
def manhattan_distance(x, y):
    return sum(abs(int(i)-int(j) for i, j in zip(x, y))
    
def euclidean_distance(x, y):
    return math.sqrt(sum(abs(int(i)-int(j)**2 for i, j in zip(x, y)))
    
def maximum_deviation(x, y):
    return max(max(abs(int(i)-int(j) for i, j in zip(x, y))

    
n = int(input())
x = input().split()
y = input().split()

print(manhattan_distance(x, y))
print(euclidean_distance(x, y))
print(maximum_deviation(x, y)