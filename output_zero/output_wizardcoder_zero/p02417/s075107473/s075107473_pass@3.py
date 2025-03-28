```python
t = ""
for i in range(10):
    try:
        t += input().lower()
    except EOFError:
        break

counts = [0]*26
for char in t:
    if ord('a') <= ord(char) <= ord('z'):
        counts[ord(char) - ord('a')] += 1

print("".join(f"{chr(i)} : {counts[i-97]} " for i in range(ord('a'), ord('z')+1)))
``` 

Explanation:
1. The program reads user input until it encounters an EOFError, which means that there is no more input left to read.
2. It stores all the lowercase letters in a string called `t`.
3. Using a for loop and ord() function, it counts the number of occurrences of each letter from 'a' to 'z'. 
4. Finally, it prints out the count of each letter separated by a space.
5. The `chr()` function is used to convert ASCII codes back to letters.
6. Instead of using two variables and a list with 26 elements, we can use a list with length 26 to store counts directly.
7. We can iterate over the range from ord('a') to ord('z'), which gives us all lowercase letters, and print the count of each letter as needed.
```
for i in range(ord('a'), ord('z')+1):
    print(chr(i), ":", counts[i-97])