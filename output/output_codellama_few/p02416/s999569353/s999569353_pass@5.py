n=int(input())
for i in range(n):
  x=str(input())
  if int(x)>0:
    print(sum([int(x[i]) for i in range(len(x))]))