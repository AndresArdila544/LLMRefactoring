import sys

s = input('').lower()
for c in s:
    if c in 'abcdefghijklmnopqrstuvwxyz':
        dic[c] = dic.get(c, 0) + 1
        
print(*[(k,v) for k,v in sorted(dic.items(), key=lambda x:x[1], reverse=True)])