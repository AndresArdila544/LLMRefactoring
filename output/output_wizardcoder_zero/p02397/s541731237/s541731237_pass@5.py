a=[]
while True:
    n = input()
    if n == '0 0': break
    x,y = map(int,n.split())
    if x>y: print(y,' ',x)
    else:print(n)