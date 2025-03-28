```python
while True:
    m, f, r = map(int, input().split())
    if m == -1 and f == -1 and r == -1:
        break
    elif (m, f) == (-1,-1):
        print('F')
    else:
        mf = m + f
        if 80 <= mf < 90:
            print('A')
        elif 65 <= mf < 80:
            print('B')
        elif 50 <= mf < 65 and r >= 50:
            print('C')
        else:
            print('D') if r < 50 else print('C')
```

This refactored code is more concise and reduces the number of lines while still maintaining its functionality. By using elif statements, we can avoid unnecessary conditions and if-else blocks for checking whether or not a certain condition is met. Additionally, using a tuple to store m and f makes it easier to check if both are -1 at once instead of separately checking for each value.