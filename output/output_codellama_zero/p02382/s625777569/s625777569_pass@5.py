import math

def manh(x, y):
    return sum(abs(int(i) - int(j)) for i, j in zip(x, y))

def uqurid(x, y):
    return math.sqrt(sum((abs(int(i) - int(j))**2 for i, j in zip(x, y))))

def minco(x, y):
    p = 3
    return (sum((abs(int(i) - int(j))**p for i, j in zip(x, y)))**(1/p))

def ebis(x, y):
    return max(sum(abs(int(i) - int(j)) for i, j in zip(x, y)), default=0)

if __name__ == '__main__':
    n = int(input())
    x = input().split()
    y = input().split()
    
    print(manh(x, y))
    print(uqurid(x, y))
    print(minco(x, y))
    print(ebis(x, y))