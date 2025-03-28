Below is the refactored version of the above program:

i = 0
while True:
        x = raw_input()
        i += 1
        if x == "0":
                break
        print 'Case %d: %s' %(i,x)