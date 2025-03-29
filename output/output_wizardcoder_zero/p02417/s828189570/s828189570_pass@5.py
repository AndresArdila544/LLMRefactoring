refactored_code = """
import sys
table = "abcdefghijklmnopqrstuvwxyz"
sentence = input().lower()
for char in table:
    print(char + ' : ' + str(sentence.count(char)))
"""