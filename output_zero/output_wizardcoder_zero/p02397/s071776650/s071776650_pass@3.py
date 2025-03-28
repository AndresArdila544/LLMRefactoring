li = list()
while True:
    a,b = map(int,input().split())
    if a==b and a==0:
        break
    li.append([a,b])
for i in sorted(li):
    print(*i)