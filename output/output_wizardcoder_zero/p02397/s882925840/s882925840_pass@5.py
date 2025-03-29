min_a = max_a = 0
while True:
    a = list(map(int,input().split()))
    if not all(a): # check for non-zero inputs
        break
    min_a,max_a = sorted([a[0], a[1]]) # sort the two numbers
    print("{} {}".format(min_a, max_a))