a,b = map(int,input().split())
print("{} {} {} {:.2f}".format(*map(str, (a//b, a%b, a/b))