S = int(input())
h, m, s = divmod(S, 360)
m, s = divmod(m, 60)
print("{}:{:02d}:{:02d}".format(h, m, s))