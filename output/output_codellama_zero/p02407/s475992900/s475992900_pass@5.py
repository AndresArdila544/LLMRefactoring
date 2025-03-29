```
num_str = input()
numlist = list(int(i) for i in num_str.split())
for j in range(len(numlist)-1):
  print(numlist[j], end=" ")
print(numlist[0])
```