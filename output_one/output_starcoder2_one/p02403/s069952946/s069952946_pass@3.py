Refactored code:

while True:
  H,W=map(int,input().split())
  if (H,W)==(0,0):
    break
  for j in range(1,H+1):
      print("#" * W)
  print()