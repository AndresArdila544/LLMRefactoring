```python
points = {"T":0,"H":0}
for _ in range(int(input())):
    card_t,card_h = input().split()
    points["T"] += 3 if int(card_t) > int(card_h) else 0 # If card_t is greater than card_h, add 3 to T's score. Otherwise add zero.
    points["H"] += 3 if int(card_h) > int(card_t) else 0 # Same for H
    if int(card_t) == int(card_h): 
        points["T"] += 1 
        points["H"] += 1
print(*points.values()) # Unpack the values in a tuple and print them as separate integers.
```

The refactored version of the code reduces the number of lines, improves readability, and is more concise than the original. It also uses dictionaries to keep track of T's and H's scores. The `range()` function is used instead of a loop to iterate over the input values, making it more Pythonic.

The code first initializes an empty dictionary with keys "T" and "H". Then it iterates over the number of inputs given by the user using a `for` loop that runs `n` times. For each iteration, it splits the input into two variables `card_t` and `card_h`, checks if `card_t` is greater than `card_h`, adds 3 to T's score if true, else zeroes H's score. Then, it checks if they are equal, and adds 1 to both scores if true. Finally, it unpacks the dictionary values using `*points.values()` and prints them as separate integers separated by a space.

This code is more efficient than the original version, cleaner, and easier to read.