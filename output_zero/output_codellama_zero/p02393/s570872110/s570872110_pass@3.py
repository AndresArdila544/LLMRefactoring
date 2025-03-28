Here is the refactored version of the original program:
```
num_sorted = list(map(int, input().split()))
print("{} {} {}".format(*sorted(num_sorted)))
```