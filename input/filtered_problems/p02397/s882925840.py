flag = True
min_a = 0
max_a = 0
while flag:
    a = list(map(int,input().split()))
    if a[0] == 0 and a[1] == 0:
        break
    if a[0] < a[1]:
        min_a = a[0]
        max_a = a[1]
    else:
        min_a = a[1]
        max_a = a[0]
    print("{} {}".format(min_a,max_a))
