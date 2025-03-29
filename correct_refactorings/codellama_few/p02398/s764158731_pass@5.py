import sys

input_list = sys.stdin.readline().split()
a = int(input_list[0])
b = int(input_list[1])
c = int(input_list[2])
count = 0

if a>=1 and b>=1 and c>=1 and 10000>=a and 10000>=b and 10000>=c:
    for i in range(a, b+1):
        if c % i == 0:
            count += 1

print(count)