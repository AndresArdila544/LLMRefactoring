def minkowski_distance(arr1, arr2, p):
    if p == 'inf':
        return max(abs(x-y) for x, y in zip(arr1, arr2))
    return pow(sum(pow(abs(x-y), p) for x, y in zip(arr1, arr2)), 1/p)