input_list = input().split(' ')
a,b,c = map(int, input_list)
print((sum(i for i in range(a, b+1) if c % i == 0)))