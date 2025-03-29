Here's a refactored version of the original program that is more concise and easier to read:

```python
word = input().lower()
texts = []
while True:
    raw_input = input()
    if raw_input == 'END_OF_TEXT':
        break
    texts.append(raw_input)
match_count = sum(' ' in line or word in line.lower() for line in texts)
print(match_count)
```

Explanation:
- The `lower()` method is used to convert the input string to lowercase, so we can compare it with the desired word in a case-insensitive manner.
- We use a list comprehension inside the sum function to count how many times the word appears in each line of the text, and then add them up to get the total count.
- The `in` keyword is used to check if the word or space appears in any line. If it does, we increment the match_count variable.
- The code terminates when we encounter a line with the string 'END_OF_TEXT' and then print out the final value of match_count.