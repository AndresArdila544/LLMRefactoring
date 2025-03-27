while True:
     ins = input().split()
     h, w = map(int, ins)
     if not h or not w: break
     for _ in range(h): print("#" * w)