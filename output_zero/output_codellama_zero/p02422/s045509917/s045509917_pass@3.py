t = input()
n = int(input())
for i in range(n):
    orders = input().split()
    order = orders[0]
    a, b = map(int, orders[1:3])
    
    if order == "replace":
        word = orders[3]
        t = t[:a] + word + t[b+1:]
    elif order == "print":
        print(t[a:b+1])
    elif order == "reverse":
        t = t[:a] + t[a:b+1][::-1]+ t[b+1:]