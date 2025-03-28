s = raw_input()
p = raw_input()
flag = all(x==y for x, y in zip(p, s))
if flag: print "Yes" else: print "No"