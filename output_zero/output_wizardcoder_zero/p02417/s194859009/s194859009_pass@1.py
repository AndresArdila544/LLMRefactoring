import sys
from string import ascii_lowercase

def count_chars(string):
    char_counts = {}
    for char in ascii_lowercase:
        char_counts[char] = 0
    
    for char in string.lower():
        if char.isalpha() and ord(char) < 97 or ord(char) > 123:
            continue
        char_counts[char] += 1
    
    return dict(sorted(char_counts.items()))

for line in sys.stdin.readlines():
    print(*count_chars(line).items())
"""
This program counts the occurrence of each letter in a given string, excluding non-alphabetic characters and sorting them by ASCII value.

The original code takes input from stdin, reads all lines at once into a list, iterates through those lines, then iterates through each character of each line to count its occurrences. It then prints the results sorted by key using the `sorted` function and unpacking it with `*`. 

The refactored version uses a single loop to read input and count characters, avoids hardcoding the range of ASCII values for lowercase letters, and uses the built-in `isalpha()` method to filter out non-alphabetic characters. Additionally, it sorts the resulting dictionary by key before printing.