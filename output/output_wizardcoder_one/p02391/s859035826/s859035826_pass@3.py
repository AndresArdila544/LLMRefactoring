a = input().split()
b = [int(e) for e in a]
if b[0] < b[1]:
 print('a < b')
elif b[0] > b[1]:
 print('a > b')
else:
 print('a == b')