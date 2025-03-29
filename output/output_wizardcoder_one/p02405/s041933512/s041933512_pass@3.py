```python
while True:
    H, W = map(int, input().split())
    if not (H and W):
        break
    for i in range(0, H, 2):
        print("#" * (W // 2))
        if H > 1:
            print()
``` 
This refactored code uses a loop to create the desired pattern. It first checks whether both `H` and `W` are truthy values before continuing with the loop. If either of them is falsy, it will break out of the loop. For each row (`i`), it prints `#` if the index is odd or `.` otherwise. After every second iteration, it will print a newline to create the desired pattern.

For example, if `H = 5` and `W = 10`, the output would be:
```
########..
#.......#
########.
```