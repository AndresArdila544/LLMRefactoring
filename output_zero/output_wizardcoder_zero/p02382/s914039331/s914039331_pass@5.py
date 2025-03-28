n = int(input())
arr1, arr2 = list(map(int, input().split())), list(map(int, input().split()))
for p in [1, 2, 'inf']:
    if p == 'inf':
        cmp_arr = max([abs(x-y) for x, y in zip(arr1, arr2)]); print(f'{cmp_arr}')
    else:
        sum_cmp_arr = sum((abs(x-y)**p for x, y in zip(arr1, arr2)); print(f'{(sum_cmp_arr)**(1/p)}')