while True:
  H,W=map(int,input().split())
  if (H,W)==(0,0):
    break
  for j in range(1,H+1):
    for i in range(1,W+1):
      print("#", end="")
    print()
  print()

