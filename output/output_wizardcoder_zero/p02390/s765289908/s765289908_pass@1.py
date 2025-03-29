s = int(input())
h, m, s = divmod(s,360)
m, s = divmod(s, 60)
print("{}:{:02d}:{:02d}".format(h,m,s))