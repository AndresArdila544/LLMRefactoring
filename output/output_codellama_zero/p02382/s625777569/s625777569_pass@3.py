def manh(x, y):
    return sum([abs(int(i)-int(j)) for i, j in zip(x,y)])

def uqurid(x, y):
    return math.sqrt(sum([(abs(int(i)-int(j)))**2 for i, j in zip(x,y)]))

def minco(x, y):
    p = 3
    return ((sum([(abs(int(i)-int(j)))**p for i, j in zip(x,y)]) ) ** (1/p))

def ebis(x, y):
    d = 0
    for i, j in zip(x, y):
        d = max(d, abs(int(i)-int(j)))
    return d