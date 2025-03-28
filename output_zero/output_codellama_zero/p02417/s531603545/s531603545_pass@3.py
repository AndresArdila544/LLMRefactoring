import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'
dic = {i:0 for i in alphabet}

for i in sys.stdin.read():
  s+=i.lower() if i in alphabet else i

for i in dic:
    print(f"{i}: {dic[i]}")