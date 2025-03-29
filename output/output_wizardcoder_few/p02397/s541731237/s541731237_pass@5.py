a=[]
while True:
    n=input()
    if n=='0 0':break
    x,y=map(int,n.split())
    a.append((x,y) if x>y else (y,x))
for i in range(len(a)):
    print(*a[i])
Refactored version:
a=[]
while True:
    try:
        n=input().split()
        if int(n[0]=='0' or int(n[1])=='0':break
        x,y=map(int,n)
        a.append((x,y) if x>y else (y,x))
    except ValueError:
        continue
for i in range(len(a)):
    print(*a[i])