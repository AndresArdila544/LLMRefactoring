x = input()
while x:
    if int(x) > 0:
        print(sum([int(i) for i in x]))
    else:
        break
    x = input()