```python
while True:
    m, f, r = map(int, input().split())
    if m == -1 and f == r == -1:
        break
    elif (m == -1) or (f == -1) or (m + f < 30):
        print("F")
    elif (m + f < 50) and (r >= 50):
        print("D")
    elif (m + f < 65) or (r >= 50):
        print("C")
    elif m + f < 80:
        print("B")
    else:
        print("A")
```
```python
while True:
    m, f = map(int, input().split())
    if m == f == -1:
        break
    elif (m == -1) or (f == -1) or (m + f < 30):
        print("F")
    elif (m + f >= 50 and r >= 50) or m + f < 65:
        print("D")
    elif m + f < 80:
        print("C")
    else:
        print("A")
```
The refactored version of the code removes unnecessary lines and simplifies the conditions. It also uses a shorter logical operator to combine the two conditions that are already checked for the same variable in line 3. Additionally, it uses tuple unpacking to assign the values directly into variables m and f rather than creating separate variables for them. The order of the if-elif statements is slightly changed to simplify the logic.