while True:
   a = sorted(map(int,raw_input().split()))
   if a == [0,0]: break
   print ' '.join(str(x) for x in a)