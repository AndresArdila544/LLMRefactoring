x = input().split()
a,b = int(x[0]),int(x[1])
print("{} < {}".format("a", "b" if a < b else "==" if a == b else ">" )