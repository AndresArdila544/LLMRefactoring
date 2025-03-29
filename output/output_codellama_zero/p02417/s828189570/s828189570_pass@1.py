Here is the refactored version of the code with fewer lines and improved readability:

import sys

table = "abcdefghijklmnopqrstuvwxyz"

sentence = sys.stdin.read()
for i in table:
    print(i + ' : ' + str(sentence.lower().count(i)))