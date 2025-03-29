def main():
    num = int(input())
    xs = [int(i) for i in input().split()]
    ys = [int(j) for j in input().split()]
    
    mh, ec, p3, cv = 0, 0, 0
    for x, y in zip(xs, ys):
        mh += abs(x - y)
        ec += (abs(x-y))**2
        p3 += (abs(x-y))**3
        cv = max(cv, abs(x-y))
    
    print("{:.8f}".format(mh), end=' ')
    print("{:.8f}".format(ec**0.5), end=' ')
    print("{:.8f}".format(p3**(1/3))
    print("{:.8f}".format(cv))