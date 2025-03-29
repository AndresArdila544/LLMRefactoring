s1 = input().upper()
print(''.join(chr(ord(c)+32) if ord('a') <= ord(c) <= ord('z') else c for c in s1)