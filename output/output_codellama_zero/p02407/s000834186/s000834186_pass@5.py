Here is a cleaner and more concise version of the original program:
```
n = int(input())
a = list(map(int, input().strip().split()))

for i in range(n-1, -1, -1):
    print(f'{a[i]} ', end='') if i else print(a[i])
```