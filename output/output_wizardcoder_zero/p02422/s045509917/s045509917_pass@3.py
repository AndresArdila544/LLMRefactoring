t = input()
n = int(input())
for _ in range(n):
    order, a, b, *rest = input().split()
    if order == "replace":
        word = rest[0]
        t = t[:a] + word + t[b+1:]
    elif order == "print":
        print(t[a:b+1])
    else: # assuming the only other possible option is "reverse"
        t = t[:a] + t[a:b+1][::-1]+ t[b+1:]