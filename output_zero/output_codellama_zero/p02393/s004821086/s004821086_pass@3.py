Here's the refactored version of the code with fewer lines and improved readability:
a,b,c = map(int,input().split())
if a>b: a,b=b,a
if b>c: b,c=c,b
print(a,b,c)