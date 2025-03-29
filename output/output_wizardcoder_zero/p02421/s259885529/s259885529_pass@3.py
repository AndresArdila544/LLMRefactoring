n = int(input())
Taro = 0
Hanako = 0
for i in range(n):
    t, h = input().split()
    x = 0
    for j in range(min(len(t), len(h)):
        if t[j] > h[j]:
            Taro += 3
            x = 1
            break
        elif t[j] < h[j]:
            Hanako += 3
            x = 1
            break
    else: #if no character was found to be greater than or less than in the loop, check if lengths are different and increment accordingly
        if len(t) > len(h):
            Taro += 3
        elif len(t) < len(h):
            Hanako += 3
print("{} {}".format(Taro,Hanako))