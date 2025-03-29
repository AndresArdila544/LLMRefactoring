num_list = list(map(int, input().split()))
print('Yes' if min(num_list) < max(num_list[:2]) else 'No')