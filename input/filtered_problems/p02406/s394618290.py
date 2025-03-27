n = int(input())

for i in range(1, n+1, 1):
    if i % 3 ==0:
        print(" ", end = "")
        print(i, end="")
    else:
        x = i
        while x:
            if x % 10 == 3:
                print(" ",end = "")
                print(i, end="")
                break
            x//=10
print()
