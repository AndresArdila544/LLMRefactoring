```python
for i in range(1, n):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if x == i + j + k:
                cnt += 1
print(cnt)
```

The program uses three nested loops to iterate through all possible combinations of `i`, `j` and `k` such that `0 <= i < j < k <= n-1`. It then checks if the sum of `i`, `j`, and `k` is equal to `x`. If it is, the counter variable `cnt` is incremented. Finally, the result is printed after all combinations have been checked.