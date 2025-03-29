t = input()
n = int(input())
for i in range(n):
    order = input().split()[0]
    a = int(input().split()[1])
    b = int(input().split()[2])
    
    if order == "replace":
        word = input().split()[3]
        t = t[:a] + word + t[b+1:]
    elif order == "print":
        print(t[a:b+1])
    else: # assuming "reverse" as the third option
        t = t[:a] + t[a:b+1][::-1]+ t[b+1:]