```python
def minkowski_distance(arr1, arr2, p):
    if p == float('inf'):
        return max([abs(x-y) for x, y in zip(arr1, arr2)
    else:
        return pow(sum([pow(abs(x-y), p) for x, y in zip(arr1, arr2)]), 1/p)


n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split())
for p in [1, 2, 3, float('inf')]:
    print(f'{minkowski_distance(arr1, arr2, p):.8f}')
```