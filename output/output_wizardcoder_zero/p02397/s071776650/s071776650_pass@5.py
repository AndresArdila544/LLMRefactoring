li = []
while True:
    a,b = map(int,input().split())
    if a==0 and b==0:
        break
    else:
        li.append([a,b])
for i in sorted(li):
    print(*i)