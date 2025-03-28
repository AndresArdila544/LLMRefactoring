flag = True
while flag:
    a = list(map(int,input().split()))
    if not all(a):
        break
    min_a, max_a = sorted([*a])
    print("{} {}".format(min_a,max_a))