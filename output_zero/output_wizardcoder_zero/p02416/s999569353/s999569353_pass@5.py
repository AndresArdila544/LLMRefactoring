```python
while True:
    x = input()
    if int(x) > 0:
        print(sum([int(c) for c in str(x)]))
    else:
        break
``` 

The `input()` function returns a string, so we can use it directly instead of converting it to an integer and then back to a string. We also don't need the `range()` function to iterate over each digit of the input number, as we can simply iterate over the characters in the string using a list comprehension.

We can remove the unnecessary assignment of `x_list` since it is only used once and directly sum the digits using another list comprehension. Finally, we use an empty list comprehension to break out of the loop if the input is less than or equal to zero.