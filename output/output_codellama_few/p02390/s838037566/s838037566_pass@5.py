import time
S = input()
h, m, s = time.gmtime(S)
print("%d:%d:%d" % (h,m,s))