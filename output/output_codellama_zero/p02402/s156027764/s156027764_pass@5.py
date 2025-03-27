number = int(input())
x = input().split(" ")
sum = 0
max = min = int(x[0])
for i in range(1, number):
    sum += int(x[i])
    if max < int(x[i]):
        max = int(x[i])
    elif int(x[i]) < min:
        min = int(x[i])
print(f'{min} {max} {sum}')