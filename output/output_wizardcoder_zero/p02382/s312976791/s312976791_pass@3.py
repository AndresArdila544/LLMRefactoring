num_list1 = list(map(int, input().split()))
num_list2 = list(map(int, input().split()))

d1 = [abs(x - y) for x, y in zip(num_list1, num_list2)]
print(sum(d1))

d2 = [(x - y)**2 for x, y in zip(num_list1, num_list2)]
print(round((sum(d2)), 3) ** (0.5))

d3 = [abs(x - y)**3 for x, y in zip(num_list1, num_list2)]
print(round((sum(d3), 3) ** (1/3))