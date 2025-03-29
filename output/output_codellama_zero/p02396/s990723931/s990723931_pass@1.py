Here is a refactored version of your code:

for i in range(MAX):
    x = int(input())
    if x == EOL:
        break
    print("Case {}: {}".format(i + 1, x))