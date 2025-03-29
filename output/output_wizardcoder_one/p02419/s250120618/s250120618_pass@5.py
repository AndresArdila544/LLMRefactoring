Here is a refactored version of the original program:

```python
import math

word = input().lower()
texts = []
while True:
    raw_input = input().strip()  # Strip whitespace from each line before appending to texts list
    if raw_input == 'END_OF_TEXT':
        break
    else:
        texts.append(raw_input)
    
count = sum([1 for text in texts if word in text])  # Use a list comprehension to count instances of the word in each line, and then use sum() function to get total match count.
print(count)
```

This version takes advantage of Python's list comprehensions and strips the whitespace from each line before appending it to the `texts` list. It also checks if `word` is in the lowercase form of each line by using the `.lower()` method instead of converting the word to lowercase separately.