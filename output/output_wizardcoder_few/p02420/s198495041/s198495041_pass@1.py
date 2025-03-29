```python
while True :
    C = input()
    if C == "-":
        break
    else:
        m = int(input())
        for i in range(m):
            h = int(input())
            c = input()[:h]
            C += c + '-'*(len(c)-1)  # Concatenate the first 'h' characters of the string and '-'s to match the length of the original string.
        print(C)
```

Explanation: The code takes an input string, `C`, and if it is not equal to "-" then it loops over a range of integers `m`. For each value of `i` in this range, it takes an integer input for `h` and appends the first `h` characters of the current iteration's input string `c` to `C`. It then pads `C` with `-` symbols so that its length is equal to the original length of `C`, effectively reversing the order of the input strings. Finally, it prints `C` in its modified form.

The refactored code reduces the number of lines by using string concatenation and slicing instead of a loop with an index variable. It also eliminates the need to store each input string in a separate variable as it is immediately added back into `C`.