Here is a refactored version of the code:
import math

def manh(x, y):
    d = 0
    for i, j in zip(x, y):
        d += abs(int(i)-int(j))
    return d

def uqurid(x, y):
    d = 0
    for i, j in zip(x, y):
        d += (abs(int(i)-int(j)))**2
    return math.sqrt(d)

def minco(x, y):
    p = 3
    d = 0
    for i, j in zip(x, y):
        d += abs((int(i)-int(j))**p)
    return d**(1/p)

def ebis(x, y):
    d = 0
    for i, j in zip(x, y):
        d = max(d, abs(int(i)-int(j)))
    return d

if __name__ == '__main__':
    n = int(input())
    x = input().split()
    y = input().split()

    print(manh(x, y))
    print(uqurid(x, y))
    print(minco(x, y))
    print(ebis(x, y))