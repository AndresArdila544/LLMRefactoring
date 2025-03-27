import sys
table = "abcdefghijklmnopqrstuvwxyz"
sentence = sys.stdin.read().lower()
for i in table:
    print(i + ' : ' + str(sentence.count(i)))