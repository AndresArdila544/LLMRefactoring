```python
a, b = map(int, input().split())
divisors = [i for i in range(a, b+1) if a % i == 0]
print(len(divisors))
```

Explanation:

The original program takes two integer inputs `a` and `b`, splits the input string by spaces into a list of numbers using the `split()` method, maps each element to an integer using the `map()` function, and then iterates over the range from `a` to `b+1`, appending all values that are divisible by `c` to the list `lst`. Finally, it prints the length of `lst`. The refactored code does the same thing in a more concise manner using a list comprehension and the ternary operator. It takes input using the `input()` method (which is equivalent to `raw_input()` in Python 2) instead of `map()`, and assigns the resulting numbers directly to variables without creating an intermediate list. Additionally, it uses a single line for the print statement by appending all values that are divisible by `c` to a new list called `divisors`. Finally, it prints the length of this new list.