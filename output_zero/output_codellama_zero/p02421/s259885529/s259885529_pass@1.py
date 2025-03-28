n = int(input())
 Taro = 0
 Hanako = 0
 for i in range(n):
    t,h = input().split()
    for j in range(min(len(t),len(h))):
        if ord(t[j]) > ord(h[j]):
            Taro += 3
        elif ord(t[j]) < ord(h[j]):
            Hanako += 3
    if len(t) > len(h):
        Taro += 3
    elif len(t) < len(h):
        Hanako += 3
 print("{} {}".format(Taro,Hanako))