a = input()
while a != "-":
    b = int(input())
    for i in range(b):
        c = int(input())
        a = a[c:] + a[:c]
print(a)