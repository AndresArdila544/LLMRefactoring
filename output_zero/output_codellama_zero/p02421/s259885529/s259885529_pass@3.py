n = int(input())
Taro = 0
Hanako = 0
for i in range(n):
    t,h = input().split()
    for j in range(min(len(t),len(h))):
        if t[j:j+1] != h[j:j+1]:
            if ord(t[j:j+1]) > ord(h[j:j+1]):
                Taro += 3
            elif ord(t[j:j+1]) < ord(h[j:j+1]):
                Hanako += 3
            break
    if len(t) != len(h):
        if len(t) > len(h):
            Taro += 3
        else:
            Hanako += 3
print("{} {}".format(Taro,Hanako))