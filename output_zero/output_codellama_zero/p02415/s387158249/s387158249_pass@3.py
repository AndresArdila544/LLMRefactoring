Here is a more concise and readable version of your original Python program:
s1 = input()
print(s2.translate({ord('a'): ord('A'), ord('A'): ord('a')}))
The translate method of strings in Python allows you to apply a lookup table to characters in the string, which is what this code does. It converts all lowercase letters to uppercase and vice versa. This is equivalent to your original code but with fewer lines and improved readability.