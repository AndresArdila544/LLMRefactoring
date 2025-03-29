```python
while True:
    H, W = map(int, input().split())
    
    if H == 0 and W == 0:
        break
    for i in range(H):
        print("#" * (W + 2)
        if i != 0 and i != H-1:
            print("." * W, end="")
            print()
``` 
Explanation:
The original code is trying to print a pattern of # for the first and last row and . for all other rows. The outer loop iterates over the height (H) and inner loop iterates over width (W). If i is 0 or H-1, then it prints # for every iteration, else it prints ..

The refactored code uses only one loop that prints # and . based on whether i is 0 or not. It also uses the * operator to repeat the string for the number of times given by W plus 2 (to include two borders) in each row and end="" parameter of print() function to join all characters without spaces between them.

```python
while True:
    H, W = map(int, input().split())
    
    if H == 0 and W == 0:
        break
    for i in range(H):
        print("#" * (W + 2)
        if i != 0 and i != H-1:
            print(".", end="")*(W)
            print() 
```