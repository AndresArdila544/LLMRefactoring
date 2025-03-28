Here is the refactored version of the program:
input_list = input().split(' ')
a, b, c = int(input_list[0]), int(input_list[1]), int(input_list[2])
count = sum(i for i in range(a, b+1) if c % i == 0)