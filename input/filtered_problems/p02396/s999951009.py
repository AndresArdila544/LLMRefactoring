a = []
tmp = 1
while(True):
  tmp  = int(input())
  if tmp == 0:
    break
  else:
    a.append(tmp)
for index,value in enumerate(a,1):
  print(f'Case {index}: {value}')
