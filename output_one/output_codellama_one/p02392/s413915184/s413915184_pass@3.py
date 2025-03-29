# Refactored Python Program
num_list = input().split()
a = int(num_list[0])
b = int(num_list[1])
c = int(num_list[2])
if a < b < c:
    print("Yes")
else:
    print("No")