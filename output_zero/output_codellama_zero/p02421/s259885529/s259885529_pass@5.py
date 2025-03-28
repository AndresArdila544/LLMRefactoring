n = int(input())
Taro=0
Hanako=0
for i in range(n):
    t,h=input().split()
    if len(t)==len(h):
        Hanako+=1
        Taro+=1
    elif len(t)<len(h):
        Hanako+=3
    else:
        Taro+=3
print("{} {}".format(Taro,Hanako))