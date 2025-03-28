Here is the refactored version of the code:

num_list=input().split()
if all(int(i)<int(j) for i, j in zip(num_list[:-1], num_list[1:])):
    print('Yes')
else :
    print('No')