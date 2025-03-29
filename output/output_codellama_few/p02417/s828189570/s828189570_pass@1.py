Here is the refactored version of the program:

import sys

table = "abcdefghijklmnopqrstuvwxyz"
sentence = input().lower()
for i in table:
    print(i + ' : ' + str(sentence.count(i)))