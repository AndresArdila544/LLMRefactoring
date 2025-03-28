while True:
    n = int(input())
    if n == 0:
        break
    a = [float(i) for i in input().split()]
    average = sum(a)/n
    print((sum([(i - average)**2 for i in a])/n) ** 0.5)

# The code is already concise and readable, but you can use f-strings to make it more concise:
while True:
    n = int(input())
    if n == 0:
        break
    a = [float(i) for i in input().split()]
    average = sum(a)/n
    print((sum([(i - average)**2 for i in a])/n) ** 0.5)