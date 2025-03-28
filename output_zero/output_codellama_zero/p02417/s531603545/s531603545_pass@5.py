import sys
alphabet = 'abcdefghijklmnopqrstuvwxyz'
dic = {i: 0 for i in alphabet}

s = ''
for i in sys.stdin.read():
    s += i
s = s.lower()

for i in s:
    if i in alphabet:
        dic[i] += 1

for i, v in dic.items():
    print(f'{i} : {v}')