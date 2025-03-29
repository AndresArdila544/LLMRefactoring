a = int(input())
h, m, s = divmod(a, 360)
print("%s:%s:%s" % (h, m, s))