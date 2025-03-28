```python
n = int(input())
taro = hana = 0
for i in range(n):
    a, b = map(str, input().split())
    if a == b:
        taro += 1
        hana += 1
    elif a < b:
        hana += 3
    else:
        taro += 3
print(taro, hana)
``` 
```python
n = int(input())
taro, hana = 0, 0
for i in range(n):
    a, b = map(str, input().split())
    taro += a == b
    hana += max(a < b, key=lambda x: int(x or 1) + 2) - 1
print(taro, hana)
``` 
In this refactored version, we initialize `taro` and `hana` to zero instead of separate lines. We then use the ternary operator in line four to set the value of `hana`. Instead of using `if` statements for each comparison, we can use a `max()` function with lambda functions to determine which operation to perform based on the condition.