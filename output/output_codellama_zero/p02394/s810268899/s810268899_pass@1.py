w, h, x, y, r = map(int,raw_input().split())
if x+r <= w and y+r <= h and x-r >= 0 and y-r >= 0:
    print "Yes"
else:
    print "No"