def minkowski_distance(arr1, arr2, p):
    if p == 'inf':
        cmp_arr = [abs(x-y) for x, y in zip(arr1, arr2)]
        return max(cmp_arr)
    sum_cmp_arr = sum([pow(abs(x-y), p) for x, y in zip(arr1, arr2)])
    return pow(sum_cmp_arr, 1/p)