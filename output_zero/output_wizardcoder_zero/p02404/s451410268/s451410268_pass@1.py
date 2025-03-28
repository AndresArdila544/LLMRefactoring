Here's a shorter solution to the problem by using string formatting and list comprehension:


```python
while True:
    num = [int(i) for i in input().split()]  # convert user input into list of integers
    H, W = map(int, num)
    if W == H == 0:  # compare both elements of the list and break if both are zero
        break
    print("#" * (W + 2) + "\n")  # first row has extra "#"
    for _ in range(H-2):  # iterate to print rows with "#"s and "."s
        print('#' + "."*(W-2) + '#\n')
print("#" * W)  # last row has only "#"
```

This version uses the `map()` function to convert the input into integers and unpacks them directly into the variables `H` and `W`. It also uses a `for` loop with a range that goes up to `H-2`, since we don't want to print the last row, which is already handled by the final `print()`. The list comprehension replaces the `"#" + "." * (W - 2) + "#\n"` string with `"#{}."*(W-1).format("#")` for each iteration of the loop. Finally, we only need one print statement at the end to print the last row.