Here is a refactored version of the original Python program:

while True:
    n = list(map(int, input().split()))
    if not (n[0] == 0 and n[1] == 0): print(" ".join(sorted(str(i) for i in n)))