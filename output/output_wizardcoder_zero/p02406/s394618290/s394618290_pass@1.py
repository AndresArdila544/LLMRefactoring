n = int(input())
for i in range(1, n+1):
    if not i % 3: print(" ", end="")
    x = i
    while x:
        if x%10 == 3:
            print("", i, end="")
            break
        x //= 10
print()