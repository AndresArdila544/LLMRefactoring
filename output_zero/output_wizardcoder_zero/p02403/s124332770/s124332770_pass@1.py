```python
while True:
    hw = input().split()
    if int(hw[0]) == 0 and int(hw[1]) == 0:
        break
    print("#" * int(hw[1] for _ in range(int(hw[0]))
```

This version of the code only has two lines, one to read input and another to print. It uses a list comprehension to generate the desired output. The `input().split()` method is used to get the height and width as separate values separated by whitespace, which are then converted into integers using int() function. The range function generates a sequence of numbers from 0 to H-1, and the print statement prints `#` character `int(hw[1])` times for each iteration in the loop.

I hope this helps! Let me know if you have any questions or need further clarification on anything.