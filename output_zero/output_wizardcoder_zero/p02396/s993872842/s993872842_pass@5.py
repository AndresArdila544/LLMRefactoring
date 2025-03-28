```python
for i in range(1, int(input()) + 1):
    print("Case {}: {}".format(i, input()))
```
This code will do the same thing as the original program but with fewer lines and improved readability. It uses a for loop instead of a while loop to iterate through the range from 1 to the value entered by the user plus one. It then prints "Case i: input()" for each iteration, where i is the current number in the loop and input() prompts the user for a new input. This approach is more concise than the original code because it eliminates the need for an if statement and counter variable. The range function replaces the while condition check and incrementing the counter.