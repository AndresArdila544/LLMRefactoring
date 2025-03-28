Here is the refactored version:

while True:
    n = list(map(int, input().split()))
    if all(x == 0 for x in n): break
    print(" ".join(sorted(n)))