```python
n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

max_diff = 0
for i in range(1, n+1):
    abs_diff = abs(x[i] - y[i])
    if abs_diff > max_diff:
        max_diff = abs_diff
    tmp = [abs_diff, abs_diff**2, abs_diff*abs_diff, 0, 0, 0, 0] + [tmp[i-1][4], tmp[i-1][5], tmp[i-1][6]] if i > 1 else [0, 0, 0]
    
    for j in range(2):
        tmp[j+3] += abs_diff + max_diff
        tmp[j+4] += abs_diff**2
        tmp[j+5] = tmp[j-1] + abs_diff*abs_diff
    
print(tmp[n][3])
print((tmp[n][4] ** (1/2)) if n else 0)
print((tmp[n][5] ** (1/3)) if n > 0 else 0)
print(max_diff) 
```

Explanation: The code defines an array `tmp` with six values for each index, where the first two values are simply the absolute difference between `x[i]` and `y[i]`. If `n>1`, it calculates the cumulative sum of these values in the third and fourth indices. Finally, it checks if the current value is greater than the maximum seen so far and updates `max_diff` accordingly.

The code then outputs the final values for the first three indices of the `tmp` array, which are used to compute other values using formulae.

```python
n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
max_diff = 0
tmp = [0]*7
for i in range(1, n+1):
    abs_diff = abs(x[i] - y[i])
    if abs_diff > max_diff:
        max_diff = abs_diff
    
    tmp.append([abs_diff, abs_diff**2, abs_diff*abs_diff, 0, 0, 0])
    if i != 1:
        for j in range(2):
            tmp[j+3] += abs_diff + max_diff
            tmp[j+4] += abs_diff**2
            tmp[j+5] = tmp[j-1] + abs_diff*abs_diff
        
    else:
        tmp[6:] = [0, 0, 0]

print(tmp[n][3])
print((tmp[n][4] ** (1/2)) if n else 0)
print((tmp[n][5] ** (1/3) if n > 0 else 0)
print(max_diff)
```