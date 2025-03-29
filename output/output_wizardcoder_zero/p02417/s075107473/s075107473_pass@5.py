```python
t = ""
while True:
    try:
        t += input().lower()
    except:
        break
for char in t:
    if ord(char) >= 97 and ord(char) <= 122:
        y[ord(char) - 97] += 1
for i in range(26):
    print(chr(i+97), ":", y[i])
``` 

Explanation: The code reads user input and stores it in a string variable `t`. It then loops through the characters in this string, converting them to lowercase and counting their frequency. Finally, it prints out each letter's count. 

The original version used two variables `y` and `x`, and one loop that checks if a character is between 97 and 123 (inclusive). The refactored code replaces the two loops with a single loop that only uses `char`. It also uses the `ord()` function to convert characters to their ASCII values, making it clearer what is being counted. Finally, it prints out each letter's count using `chr(i+97)` instead of hard-coding the letters A-Z and subtracting 97.