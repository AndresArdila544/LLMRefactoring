Here is a more concise version of your original code:

a, b = map(int, input().split())
if a < b:
    print("{} < {}".format('a', 'b'))
elif a > b:
    print("{} > {}".format('a', 'b'))
else:
    print("{} == {}".format('a', 'b'))