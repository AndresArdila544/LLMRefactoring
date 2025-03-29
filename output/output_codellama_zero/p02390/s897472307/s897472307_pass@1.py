def time_converter(time):
    h = int(time / 3600)
    m = int((time - h * 3600) / 60)
    s = int((time - h * 3600) % 60)
    return str(h) + ':' + str(m) + ':' + str(s)