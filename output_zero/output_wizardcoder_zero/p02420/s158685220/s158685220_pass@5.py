```python
import sys

letters = ""
m = h = 0
for line in sys.stdin:
    if m == 0 and not letters:
        letters = line.strip()
    elif m != 0 and h == 0:
        h = int(line)
    else:
        m -= 1
        print(letters[h:] + letters[:h]) if m > 0 else print(letters) 
```

In this version, the code reads the input from `sys.stdin` and stores it in a variable called `letters`. Once the value of `m` is non-zero, it checks if `h` has been set to an integer value yet or not.
If `h` hasn't been set yet, then we just set its value with the input from the user. 

If `h` has been set, then we check whether `m` is greater than 0 and if so, we concatenate the first half of `letters` (from index `h`) to the end of it (`letters[h:]`), with the second half of `letters` from the beginning (`letters[:h]`) to print the rotated string. If not, we just print `letters`. We also decrement `m` by 1.

The code is now reduced in lines and more readable since it only requires one loop instead of three, and we have combined the two if-elif statements into a single condition for improved readability.