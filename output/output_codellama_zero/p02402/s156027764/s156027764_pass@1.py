number = int(input())
x = input().split(" ")
sum = max = min = x[0]
for i in range(1, number):
    sum += int(x[i])
    max = max if max > int(x[i]) else int(x[i])
    min = min if min < int(x[i]) else int(x[i])
print(f"{min} {max} {sum}")