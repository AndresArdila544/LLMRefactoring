Here is the refactored version of the code:

a = int(input())
h, m, s = (a//3600, (a-h*3600)//60, a-((h*3600)+(m*60)))
print("%s:%s:%s" % (h, m, s))