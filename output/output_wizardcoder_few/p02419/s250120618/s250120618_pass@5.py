```python
word = input().lower()
texts = []
while True:
    raw_input = input().lower()
    if raw_input == 'end_of_text':  # note that I converted `END_OF_TEXT` to lowercase for consistency with the next line and all other lowercase words
        break
    texts.append(raw_input)
    
match_count = sum(1 for line in texts if word in line)  # using a generator expression to count matches and avoid creating a new list of lines that we won't use anyway
print(match_count)
```