def format_time(a):
    h = int(a / 3600)
    m = int((a - h * 3600) / 60)
    s = int(a - (h * 3600) - (m * 60))
    return "%s:%s:%s" % (h, m, s)

print(format_time(int(input())))