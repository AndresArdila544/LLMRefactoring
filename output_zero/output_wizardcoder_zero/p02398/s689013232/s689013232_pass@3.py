a = int(input())
b = int(input())
count = sum([1 for i in range(a, b+1) if a % i == 0 or b % i == 0])-2
print(count)