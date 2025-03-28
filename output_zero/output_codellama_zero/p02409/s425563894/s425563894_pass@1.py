```
# Refactored Python Program

n = int(input())
a = [[0 for _ in range(10)] for _ in range(3)]

for b, f, r, v in zip(*[map(int, input().split()) for _ in range(n)]):
    a[b-1][f-1][r-1] += v

for c in range(4):
    print('', *a[c][:3])
    if c != 3:
        print('#' * 20)
```