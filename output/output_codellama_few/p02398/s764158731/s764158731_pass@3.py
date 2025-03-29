input_list = input().split(' ')
a = int(input_list[0])
b = int(input_list[1])
c = int(input_list[2])

if 1 <= a < 10000 and 1 <= b < 10000 and 1 <= c < 10000:
    for i in range(a, b+1):
        if c % i == 0:
            count += 1
print(count)