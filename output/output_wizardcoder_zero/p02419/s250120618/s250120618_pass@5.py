```python
import string 

texts = []
while True:
    line = input().lower()
    if line == 'END_OF_TEXT':
        break
    texts.append(line)
words = [word for text in texts for word in text.split()]
count = sum([1 for word in words if word == word.lower()]) 
print(count)
```