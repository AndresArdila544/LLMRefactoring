import sys

num = int(input())

for i in range(1, num+1):
    if i % 3 == 0:
        print(i, end="")
    elif "3" in str(i):
        print(i, end="")
print("")