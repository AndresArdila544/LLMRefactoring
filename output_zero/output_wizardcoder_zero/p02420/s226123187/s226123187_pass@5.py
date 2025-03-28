```python
cards = ""
while True:
    e = input()
    if e == "-":
        break
    cards += input() + " " * (int(input()) - 1)
print(cards[:-1])
```

Explanation: The original code takes input from the user in chunks of two lines. It first asks for the number of characters to be added to the string, and then asks for that many characters as input. However, we can simply concatenate the string by multiplying it with the integer value obtained using `input()`, which will give us the same result. So instead of looping over a range from 0 to `m-1`, we can use `int(input())` and multiply the string with that number to get the desired result.

Then, the code simply removes the last character in the resulting string by slicing the string from index 0 to the second last one. This is achieved using `[:-1]`.