Here is the refactored Python program:

input_list = input().split(' ')
a, b, c = map(int, input_list)
count = sum(i for i in range(a, b+1) if c % i == 0)
print(count)