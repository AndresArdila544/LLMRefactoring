import datetime as dt
t = input()
d = int(t[0:2])
h = int(t[3:5])
m = int(t[6:8])
s = int(t[9:])

print('%s:%s:%s' % (d + h * 1440 + m * 60 + s, dt.timedelta(seconds=d*24*3600+h*3600+m*60+s).time()))