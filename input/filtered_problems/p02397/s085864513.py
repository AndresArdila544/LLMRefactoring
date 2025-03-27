while True:
  a = map(int,raw_input().split())
  a.sort()
  if a == [0, 0]: break

  for x in a:
    print x,
  print

