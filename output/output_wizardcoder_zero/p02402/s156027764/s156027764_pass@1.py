number = int(input())
x = input().split(" ")
sum = 0
max_num = min_num = int(x[0])
for i in range(1, number):
    sum += int(x[i])
    if max_num < int(x[i] > min_num:
        max_num = int(x[i])
    elif int(x[i] < min_num:
        min_num = int(x[i])
print(str(min_num)+" "+str(max_num)+" "+str(sum))