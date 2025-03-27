num = input().split()
num.sort()
for i in num:
    print(int(i) , end="")
    if i != num[len(num) - 1]:
        print(" " , end="")