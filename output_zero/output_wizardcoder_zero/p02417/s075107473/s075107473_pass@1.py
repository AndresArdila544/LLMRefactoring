```python
import string

def count_letters(input_string):
    y = [0]*26  # initialize the list with all values set to zero
    for char in input_string.lower():
        if char.isalpha():
            y[ord(char)-97] += 1 # add one to the corresponding index of the character in y list 
    print("".join([f"{chr(i+97)} : {y[i-96]} " for i in range(97,123) if y[i-96]])

# example usage: count_letters("Hello World!")
```