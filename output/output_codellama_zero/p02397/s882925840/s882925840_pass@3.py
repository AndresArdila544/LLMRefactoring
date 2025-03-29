Here is a Python program that works as intended but has been refactored for fewer lines and improved readability:

flag = True
while flag:
    a = list(map(int, input().split()))
    if not all([a[0] == 0, a[1] == 0]):
        min_a = min(a)
        max_a = max(a)
        print("{} {}".format(min_a, max_a))