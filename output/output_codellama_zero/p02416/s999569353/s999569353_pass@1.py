while True:
  x = str(input())
  if x == '':
    break
  else:
    x_list = [int(x[i]) for i in range(len(x))]
    print(sum(x_list))