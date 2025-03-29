import sys
table = "abcdefghijklmnopqrstuvwxyz"
sentence = input().lower()
for i in table:
    print(f'{i} : {sentence.count(i)}')