Here is a refactored version of your Python program:

N = list(map(int, input().split()))
for i in range(0, N[0]): # H
    if i == 0 or i == (N[0] - 1):
        print("#" * (N[1]-2) + "#")
    else:
        print(".#"*(N[1]-2) + ".#")
print("")