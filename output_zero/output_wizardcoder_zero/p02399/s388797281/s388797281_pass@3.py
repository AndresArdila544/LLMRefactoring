a,b = map(int, input().split())
print("{0:10.20f}".format(float(a / b), end=' ') # use float instead of int to avoid truncating decimals and remove trailing newline with end argument