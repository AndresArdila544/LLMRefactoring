a = int(input())
b = int(input())
c = int(input())
print((b-a+1) - sum([i%c!=0 for i in range(a, b+1)]))