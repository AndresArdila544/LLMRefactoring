import fileinput
T = dict((chr(i),0) for i in range(26))
for line in fileinput.input():
 S=list(map(int,line.encode()))
 for c in S:
  if 65<=c<=90:
   T[chr(c)]+=1
  elif 97<=c<=122:
   T[chr(c)]+=1
for i in range(97,123):
 print(f"{chr(i)}:{T[chr(i)]}")