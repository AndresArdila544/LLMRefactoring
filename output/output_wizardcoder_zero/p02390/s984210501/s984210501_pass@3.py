def time_to_hms(a):
    print("{0}:{1}:{2}".format(a//3600, a%3600//60, a%60))