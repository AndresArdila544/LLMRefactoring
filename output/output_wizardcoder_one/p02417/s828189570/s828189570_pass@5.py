refactored_version = """
import sys
table = "abcdefghijklmnopqrstuvwxyz"
sentence = input()
for i in table:
    print(i + ' : ' + str(sentence.lower().count(i)))
""" 
print(refactored_version)