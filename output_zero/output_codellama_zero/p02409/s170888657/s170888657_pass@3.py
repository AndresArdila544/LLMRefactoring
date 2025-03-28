Here is a refactored version of the original Python program:

data = [[[0 for r in range(10)] for f in range(3)] for b in range(4)]
count = int(input())
for c in range(count):
    b, f, r, v = [int(i) for i in input().split()]
    data[b-1][f-1][r-1] += v
    
for bi, b in enumerate(data):
    print('#' * 20 if bi < 3 else '', end='')
    for f in b:
        print(''.join(str(r) for r in f), end='')
        print()