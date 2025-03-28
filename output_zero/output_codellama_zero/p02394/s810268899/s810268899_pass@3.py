w,h,x,y,r=map(int,raw_input().split())
if x>=r and y>=r:
    if x<=w-r and y<=h-r:
        print "Yes"
    else:
        print "No"