import sys
alphabet='abcdefghijklmnopqrstuvwxyz'
dic={}
for i in alphabet:
  dic[i]=0


s=''
for i in sys.stdin.read():
  s+=i
s=s.lower()

for i in s:
  if i in alphabet:
    dic[i]+=1

for i in dic:
  print(f'{i} : {dic[i]}')
