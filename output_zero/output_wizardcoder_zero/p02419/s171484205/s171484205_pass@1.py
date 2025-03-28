# Using set() to count occurrences of word in a list while ignoring case sensitivity.
word = input().lower()
count = sum(1 for i in map(str.lower, stdin.read().split()) if i == word)