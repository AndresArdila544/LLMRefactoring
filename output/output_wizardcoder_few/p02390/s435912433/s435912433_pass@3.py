h = int(input())
m, s = divmod(h, 360)
m1, s = divmod(m, 60)
print("{}:{:02d}:{:02d}".format(h, m1, s))