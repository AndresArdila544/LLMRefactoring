Here's a refactored version of the given code in two separate functions:

```python
import math

def count_matches(word):
    texts = []
    while True:
        raw_input = input()
        if raw_input == 'END_OF_TEXT':
            break
        texts.append(raw_input.lower())
    
    def count_matches_in_line(text, word):
        matches = 0
        for w in text.split(' '):
            if w == word.lower():
                matches += 1
        return matches
    
    match_count = sum(count_matches_in_line(text, word) for text in texts)
    print(match_count)
```
This code defines a function `count_matches` that takes a word as input and uses it to count the number of occurrences of that word in all lines. It then loops through each line and counts the matches using another helper function, `count_matches_in_line`, which is defined within the `count_matches` function.

This code is more modular and easier to read than the original code, as it separates the two tasks into separate functions. It also uses a list comprehension to simplify the loop logic. Finally, the `sum()` function is used to tally up all of the counts from each line in one line instead of using a for loop.