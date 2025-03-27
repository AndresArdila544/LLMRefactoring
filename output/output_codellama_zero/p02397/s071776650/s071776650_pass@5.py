li = []
while True:
    a,b = map(int,input().split())
    if not (a==b and a==0):
        li.append(sorted([a,b]))
for a,b in li:
    print(a,b)