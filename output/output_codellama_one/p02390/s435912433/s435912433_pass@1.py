a = int(input())
d = a // 3600
m = (a - d * 3600) // 60
s = a - d * 3600 - m * 60
print("%d:%d:%d" % (h, m, s))