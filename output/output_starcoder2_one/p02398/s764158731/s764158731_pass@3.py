Here is the refactored version of the code:

a = int(input())
b = int(input())
c = int(input())
count = 0

if 1<=a and b<=10000 and c<=10000:
    for i in range(a, b+1):
        if c % i == 0:
            count += 1
    
print(count)