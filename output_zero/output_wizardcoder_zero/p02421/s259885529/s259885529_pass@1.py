n = int(input())
Taro = Hanako = x = 0
for i in range(n):
    t, h = input().split()
    for j in range(min(len(t), len(h)):
        if not x and (ord(t[j:j+1]) > ord(h[j:j+1] or ord(t[j:j+1]) < ord(h[j:j+1])):
            Taro += 3 * int((len(t) > len(h)) - (len(t) < len(h))) + 1
            Hanako += 3 * int((len(h) > len(t)) - (len(t) < len(h))) + 1
    x = 1
print("{} {}".format(Taro, Hanako))
# Refactored version of the code. Removed unnecessary break statements and reduced lines.