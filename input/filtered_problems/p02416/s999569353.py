while True:
  x=str(input())
  if int(x)>0:
    x_list=[int(x[i]) for i in range(len(x))]
    print(sum(x_list))
  else:
    break
