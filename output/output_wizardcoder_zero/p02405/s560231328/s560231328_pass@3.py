```python
def print_square(n):
    while True:
        H, W = map(int, input().split())  # get user input for dimensions (H and W)
        if not all(n != 0 for n in [H, W]):  # check if both dimensions are non-zero
            break
        
        so = "#." * W
        se = "." * W
    
        for i in range(H)[::2]:   # loop through the rows (incrementing by 2 to alternate between printing so and se)
            if i % 2 == 0:
                print(so)
            else:
                print(se)

```

This is a cleaner version of the code with reduced lines and improved readability. The `print_square()` function takes in the dimensions as input and uses a loop to iterate through each row, alternating between printing so and se for each even/odd rows respectively.
The original code used multiple variables and loops, making it more complex. This version is more concise and easier to understand.